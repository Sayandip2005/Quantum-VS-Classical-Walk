import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer

def build_quantum_walk_circuit(steps):
    num_position_qubits = int(np.ceil(np.log2(2 * steps + 1)))
    if num_position_qubits == 0 and steps > 0:
        num_position_qubits = 1
    num_qubits = num_position_qubits + 1
    qc = QuantumCircuit(num_qubits, num_position_qubits)
    coin_qubit = 0
    position_qubits = list(range(1, num_qubits))
    steps_binary = bin(steps)[2:].zfill(num_position_qubits)
    for i in range(num_position_qubits):
        if steps_binary[num_position_qubits - 1 - i] == '1':
            qc.x(position_qubits[i])
    qc.h(coin_qubit)
    for _ in range(steps):
        qc.x(coin_qubit)
        qc.cx(coin_qubit, position_qubits[0])
        for i in range(num_position_qubits - 1):
            qc.ccx(coin_qubit, position_qubits[i], position_qubits[i + 1])
        qc.x(coin_qubit)
        qc.x(position_qubits)
        qc.cx(coin_qubit, position_qubits[0])
        for i in range(num_position_qubits - 1):
            qc.ccx(coin_qubit, position_qubits[i], position_qubits[i + 1])
        qc.x(position_qubits)
        qc.h(coin_qubit)
    qc.measure(position_qubits, range(num_position_qubits))
    return qc

def simulate_quantum_walk(qc, shots, num_position_qubits):
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)
    positions, probabilities = [], []
    total_counts = sum(counts.values())
    offset = 2 ** (num_position_qubits - 1) if num_position_qubits > 0 else 0
    for bit_string, count in counts.items():
        position_int = int(bit_string, 2)
        position = position_int - offset
        positions.append(position)
        probabilities.append(count / total_counts)
    positions = np.array(positions)
    probabilities = np.array(probabilities)
    sort_indices = np.argsort(positions)
    return positions[sort_indices], probabilities[sort_indices]
