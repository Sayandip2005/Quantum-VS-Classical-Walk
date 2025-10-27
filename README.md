# 🧭 Classical vs Quantum Random Walk Simulation

This project demonstrates the difference between **classical** and **quantum** random walks by simulating both and comparing their probability distributions.  
It visually illustrates how **quantum superposition** and **interference** lead to fundamentally different outcomes compared to classical randomness.

---

## 🎯 Objective
To compare how probability distributions evolve in **classical** versus **quantum** walks and to highlight the advantage of quantum systems — faster spreading and unique interference patterns.

---

## ⚙️ Key Features
- ✅ Simulation of **1D Classical Random Walk**
- ✅ Construction of **Quantum Walk Circuit** using **Hadamard Coin**
- ✅ Execution using **Qiskit Aer Simulator**
- ✅ **Probability Distribution Visualization** with Matplotlib
- ✅ Comparative analysis of Classical and Quantum behaviors

---

## 🧠 Concept Overview
This project explores and compares the behavior of a Classical Random Walk and a Quantum Walk on a one-dimensional line.

In a Classical Random Walk, a particle moves either left or right at each step, determined by random probability (like flipping a fair coin). Over many steps, this randomness produces a binomial, bell-shaped distribution centered around the origin. The spread of this distribution grows proportionally to the square root of the number of steps, representing a diffusive process.

In contrast, a Quantum Walk utilizes the principles of quantum superposition and interference. The particle simultaneously exists in both left and right states, with its evolution governed by unitary operations such as the Hadamard and shift gates. This results in constructive and destructive interference, forming an asymmetric, double-peaked distribution that spreads much faster — linearly with the number of steps.

The difference in how the two walks spread reveals the computational advantage of quantum mechanics. While classical walks spread slowly and diffusively, quantum walks propagate ballistically, allowing information to travel faster. This property forms the foundation for several quantum algorithms, including Grover’s search and quantum transport models.

Quantum walks form the foundation of several **quantum algorithms** such as Grover’s search and element distinctness.  
This project provides an intuitive understanding of how quantum mechanics alters computation and probability dynamics.

---

## 🧰 Technologies Used
- Python 3.x  
- Qiskit  
- NumPy  
- Matplotlib  

---

## 🚀 Setup & Execution

- Clone the repository
- git clone https://github.com/Sayandip2005/Quantum-VS-Classical-Walk

- (Optional) Create and activate a virtual environment
- python -m venv venv
- source venv/bin/activate       # macOS/Linux
- venv\Scripts\activate        # Windows

- Install dependencies
- pip install -r requirements.txt

- Run the simulation
- python src/main.py

- The result plot will open automatically and be saved at: results/plots




## See the Results section for comparative probability plots of Classical and Quantum walks.








