import time
import matplotlib.pyplot as plt
from classical_walk import simulate_classical_walk
from quantum_walk import build_quantum_walk_circuit, simulate_quantum_walk


def main():
    steps = 4
    trials = 1024

    # Run classical random walk
    classical_positions, classical_probabilities = simulate_classical_walk(steps, trials)

    # Run quantum random walk
    quantum_circuit = build_quantum_walk_circuit(steps)
    num_position_qubits_qc = quantum_circuit.num_qubits - 1
    quantum_positions, quantum_probabilities = simulate_quantum_walk(
        quantum_circuit, trials, num_position_qubits_qc
    )

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.bar(classical_positions - 0.2, classical_probabilities, width=0.4,
            label='Classical Walk', alpha=0.7)
    plt.bar(quantum_positions + 0.2, quantum_probabilities, width=0.4,
            label='Quantum Walk', alpha=0.7)
    plt.xlabel("Position")
    plt.ylabel("Probability")
    plt.title("Classical vs Quantum Random Walk Probability Distributions")
    plt.legend()

    # Save plot with a unique timestamped filename
    timestamp = int(time.time())
    save_path = f"results/plots/comparison_plot_steps_{steps}_{timestamp}.png"
    plt.savefig(save_path)

    print(f"\n✅ Plot saved successfully at: {save_path}\n")
    plt.show()


if __name__ == "__main__":
    main()
