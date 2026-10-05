# Numerix Lab — Python Computational Laboratory Manual

This directory contains standalone, pure Python implementations of all mathematical algorithms featured in **NUMERIX LAB**, designed specifically for academic evaluation and viva voce demonstrations.

---

## 📂 Laboratory Scripts Overview

| Script Name | Mathematical Algorithm | Key Formulation / Invariant |
| :--- | :--- | :--- |
| **`01_thermal_solver.py`** | 2D Poisson Heat Equation | 5-point central stencil, Jacobi vs. Gauss-Seidel convergence comparison, spectral radius $\rho(G_{GS}) = [\rho(G_J)]^2$. |
| **`02_pagerank_power_iteration.py`** | Spectral Graph Theory & PageRank | Column-stochastic transition matrix $M$, Google matrix $G = \alpha M + \frac{1-\alpha}{N}E$ ($\alpha=0.85$), Power Iteration for $\lambda_1 = 1.0$. |
| **`03_root_finding_bisection_newton.py`** | Non-Linear Root Finding | Bisection (Linear $O(1/2^n)$) vs. Newton-Raphson (Quadratic $O(\epsilon^2)$), tangent line extrapolation, tolerance checks. |
| **`04_eigenvalue_eigenvector_solver.py`** | Spectral Matrix Decomposition | Analytical $\det(A - \lambda I) = 0$, Trace invariant ($\sum \lambda_i = \text{Tr}(A)$), Determinant invariant ($\prod \lambda_i = \det(A)$), Unit eigenvectors. |
| **`run_all_experiments.py`** | Master CLI Menu Runner | Interactive terminal runner to execute any experiment live in front of the examiner. |

---

## 🚀 How to Run in VS Code

### Option 1: Master Interactive Menu
Open the VS Code Terminal (`Ctrl + ~`) and type:
```bash
python python_lab/run_all_experiments.py
```
This will launch an interactive menu allowing you to pick and run any experiment live.

### Option 2: Run Individual Experiments
```bash
# 1. Thermal Solver (Generates side-by-side heatmaps and log-residual curves)
python python_lab/01_thermal_solver.py

# 2. PageRank Power Iteration (Prints step-by-step matrix trace and bar chart)
python python_lab/02_pagerank_power_iteration.py

# 3. Root Finding (Prints step-by-step table comparing Bisection vs Newton)
python python_lab/03_root_finding_bisection_newton.py

# 4. Eigenvalue & Invariants Verification (Analytical proof and null space basis)
python python_lab/04_eigenvalue_eigenvector_solver.py
```

---

## 👨‍🏫 Critical Viva Questions & Answers for Sir

### 1. Why does Gauss-Seidel converge twice as fast as Jacobi in `01_thermal_solver.py`?
> **Answer:** For 2-cyclic consistently ordered matrices (like the 5-point discrete Laplacian), the spectral radii satisfy:
> $$\rho(G_{GS}) = [\rho(G_J)]^2$$
> Since $\rho < 1$, squaring it cuts the dominant error factor, doubling the asymptotic rate of convergence $R_\infty = -\ln(\rho)$. Thus, Gauss-Seidel achieves the same tolerance in approximately half the iterations.

### 2. Why is damping factor $\alpha = 0.85$ used in `02_pagerank_power_iteration.py`?
> **Answer:** Real networks have "spider traps" (loops that trap rank) and "dead ends" (nodes with 0 outgoing links). Introducing $\alpha = 0.85$ guarantees that the Google matrix $G$ has strictly positive entries ($G_{ij} > 0$), satisfying the **Perron-Frobenius Theorem**. This guarantees a unique dominant eigenvalue $\lambda_1 = 1.0$ and bounds the second eigenvalue by $|\lambda_2| \le \alpha = 0.85$, ensuring fast exponential convergence $O(0.85^k)$.

### 3. What is the fundamental difference in convergence order in `03_root_finding_bisection_newton.py`?
> **Answer:** 
> - **Bisection:** First-order / Linear convergence ($p = 1$). The error decreases by a factor of 2 each step: $\epsilon_{n+1} = \frac{1}{2}\epsilon_n$. It is unconditionally guaranteed by the Intermediate Value Theorem.
> - **Newton-Raphson:** Second-order / Quadratic convergence ($p = 2$). The error satisfies $\epsilon_{n+1} \approx C \cdot \epsilon_n^2$. Near the root, it doubles the number of significant digits in every single iteration.

### 4. How do you verify eigenvalue correctness in `04_eigenvalue_eigenvector_solver.py`?
> **Answer:** Using matrix algebraic invariants:
> 1. The sum of eigenvalues equals the matrix trace: $\sum_{i=1}^n \lambda_i = \text{Tr}(A) = \sum a_{ii}$.
> 2. The product of eigenvalues equals the matrix determinant: $\prod_{i=1}^n \lambda_i = \det(A)$.
