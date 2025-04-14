# 📐 Mathematical Methods and Models – Lab Series

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-Mathematical%20Models%20%26%20Optimization-purple)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Focus](https://img.shields.io/badge/Focus-Linear%20Programming%2C%20Game%20Theory%2C%20Portfolio%20Optimization-orange)]()

This repository contains the laboratory work for the **Mathematical Methods and Models** course in the Master’s
curriculum. The labs cover a broad range of optimization techniques, from linear programming and transportation problems
to game theory and financial modeling.

---

## 📊 Lab Overview

### 🧮 Lab I – Linear Programming: Maximization & Minimization

**Focus**: Solving linear programming problems using `scipy.optimize.linprog`.

- **Minimization Task**: Cost-efficient staff allocation across multiple shifts.
- **Maximization Task**: Revenue maximization through ticket-type optimization.
- Techniques: Simplex method, constraint setup, variable bounding.

📄 Files:

- `Laboratorul I - maximizare.py`
- `Laboratorul I - minimizare.py`

---

### 🚚 Lab II – Balanced & Unbalanced Transportation Models

**Focus**: Implementing and solving transportation problems using the `pulp` library.

- **Balanced Model**: Matching fabric supply to depot demand.
- **Unbalanced Model**: Supply/demand imbalance handled with dummy nodes.
- Techniques: Linear constraints, integer optimization, cost minimization.

📄 Files:

- `Laboratorul II - echilibrat.py`
- `Laboratorul II - neechilibrat.py`

---

### 🎲 Lab III – Game Theory Models

**Focus**: Applying maxmin, minimax strategies, and solving mixed/pure strategy problems.

- **Pure Strategies**: Optimal moves for both players based on payoff matrix analysis.
- **Mixed Strategies**: Solving linear programs to find optimal mixed strategies and expected profit.

📄 Files:

- `Laboratorul III - pure.py`
- `Laboratorul III - mixte.py`

---

### 💰 Lab IV – Portfolio Risk and Optimization

**Focus**: Financial modeling with real market data.

- **Preprocessing**: Aggregating and aligning price series from multiple companies.
- **Risk Calculation**: Expected return, volatility, and Sharpe ratio using covariance matrices.
- Techniques: Portfolio theory, matrix algebra, NumPy/Pandas automation.

📄 Files:

- `Laboratorul IV - preprocess.py`
- `Laboratorul IV - risk.py`

---

## 🛠 Technologies Used

- Python 3.10+
- `scipy.optimize`, `pulp`
- `NumPy`, `Pandas`
- `Matplotlib`
- Linear algebra & optimization techniques

---

## 📁 Repository Structure

```
📂 Lab I
 ├── Laboratorul I - maximizare.py
 └── Laboratorul I - minimizare.py

📂 Lab II
 ├── Laboratorul II - echilibrat.py
 └── Laboratorul II - neechilibrat.py

📂 Lab III
 ├── Laboratorul III - pure.py
 └── Laboratorul III - mixte.py

📂 Lab IV
 ├── Laboratorul IV - preprocess.py
 └── Laboratorul IV - risk.py
```

---

## 📄 License

This project is licensed under the MIT License.
