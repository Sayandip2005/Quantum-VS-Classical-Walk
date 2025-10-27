import numpy as np

def simulate_classical_walk(steps, trials):
    final_positions = np.zeros(trials, dtype=int)
    for i in range(trials):
        current_position = 0
        for _ in range(steps):
            move = np.random.choice([-1, 1])
            current_position += move
        final_positions[i] = current_position
    unique_positions, counts = np.unique(final_positions, return_counts=True)
    probabilities = counts / trials
    return unique_positions, probabilities
