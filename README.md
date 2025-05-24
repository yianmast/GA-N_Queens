# 🧬 Genetic Algorithm for Solving the N-Queens Puzzle

This project uses a **Genetic Algorithm** to find a solution to the classic **N-Queens** problem — placing N queens on an N×N chessboard so that no two queens attack each other.

## 📌 Features

- Genetic algorithm with:
  - Customizable population size and crossover point
  - Mutation for genetic diversity
  - Fitness function based on conflict count
- Tkinter-based GUI to display the solution
- Matplotlib visualization of fitness evolution per generation

---

## 🚀 How It Works

1. **Initialize Population**: A list of random board configurations is created.
2. **Evaluate Fitness**: Fitness is based on the number of non-conflicting queen pairs.
3. **Select Parents**: The top 50% of the population (by fitness) are selected.
4. **Crossover**: Parents are crossed at user-defined points to create offspring.
5. **Mutation**: Offspring are randomly mutated to introduce variation.
6. **Repeat**: Process continues until a perfect solution is found (no conflicts).

---

## 🧠 Fitness Function

The fitness is calculated as: fitness = max_possible_non_attacking_pairs - (horizontal_collisions + diagonal_collisions)


Where:
- `max_possible_non_attacking_pairs = N * (N - 1) / 2`

---

## 📊 Output

- **Text**: Best chromosome and fitness in each generation
- **GUI**: Tkinter-based chessboard showing the solution
- **Plot**: Line chart showing best fitness (%) over generations

---

## 💻 Requirements

- Python 3.6+
- `tkinter` (standard with Python)
- `matplotlib`

Install with: pip install matplotlib  

## ▶️ How to Run
python n_queens_genetic.py  
You will be prompted to enter:

The board size (N > 3)

A crossover point (e.g., 3)

## 🛠️ Customization
You can tweak:

Population size: Currently 2 * N^2

Crossover logic: Use multi-point or uniform crossover

Mutation rate: Modify how frequently mutation occurs

## 📚 Related Concepts
Evolutionary Algorithms

Fitness Landscape

Local Optima vs Global Optimum

NP-Complete Problems

## 📄 License
This project is licensed under the MIT License.

## 👤 Author
Ioannis Mastoras

