# NUMERIX LAB — “Numerical Methods, Visualized.”

A computational simulation platform and academic laboratory showcasing numerical algorithms with interactive telemetry and design.

---

## 🚀 Quick Start (Local Execution)

NUMERIX LAB is completely self-contained (zero external npm dependencies required to run). You can run it instantly using any of the following methods:

### Option 1: Python HTTP Server (Already active or run locally)
```bash
python -m http.server 3000
```
Then open: **`http://localhost:3000`** in your browser (Chrome or Edge recommended).

### Option 2: Node.js `npx serve`
```bash
npx serve .
```

### Option 3: Direct File Execution
Double click [index.html](file:///C:/Users/great/OneDrive/Desktop/Proogram/index.html) in your browser.

---

## ⚡ Flagship Modules & Mathematical Features

### 1. 🔥 THERMALX (Thermal Field Dynamics & Optimization)
- **Mathematical Model:** 2D steady-state finite-difference heat diffusion (Poisson equation: $k \nabla^2 T + Q - h_{\text{conv}}(T - T_{\text{amb}}) = 0$).
- **5-Point Stencil Formulation:**
  $$T_{i,j}^{(k+1)} = \frac{T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1} + \frac{h^2}{k} Q_{i,j} + H \cdot T_{\text{amb}}}{4 + H}$$
- **Jacobi vs. Gauss-Seidel:**
  - *Jacobi:* Updates $T^{(k+1)}$ strictly from iteration $k$.
  - *Gauss-Seidel:* Immediately reuses newly computed values in-place within the current scan, converging approximately twice as fast.
- **Interactive Laptop Motherboard Simulation:**
  - Configurable Ambient (15°C–40°C), CPU (40°C–105°C), GPU (40°C–100°C), Battery (20°C–60°C), and Cooling Convection (0%–100%).
  - Live animated solving engine with real residual error tracking $\|T^{(k+1)} - T^{(k)}\|_\infty$.
  - High-precision thermal canvas with smooth color interpolation, heat pipes, chip outlines, and **live coordinate hover probe** $(x, y) \to T(x, y)$.
- **Bisection Thermal Optimization:**
  - Automatically applies the Bisection method on interval $[0\%, 100\%]$ cooling to find the minimal cooling intensity satisfying $T_{\max} \le 75.0^\circ\text{C}$.
- **Custom Grid CAD Designer:**
  - 16x16 interactive grid canvas with placement tools: Heat Source, Cooling Sink, Eraser, and Cell Inspector.
- **Thermal Challenges:**
  - Real scenarios (e.g., "Cool the System below 75°C" using fan, heatsink conduction, and ventilation).

---

### 2. 🌐 LINKRANK (Network Influence & Centrality)
- **Mathematical Model:** Column-stochastic transition matrix and Google matrix formulation:
  $$G = d \mathbf{M} + \frac{1-d}{N} \mathbf{J}_{N \times N}$$
- **Perron-Frobenius Theorem & Power Iteration:**
  - The dominant eigenvalue is $\lambda_1 = 1.000$.
  - Computes the stationary probability distribution (dominant eigenvector) via $v^{(k+1)} = G v^{(k)}$.
- **Force-Directed Network Graph Visualizer:**
  - Physics simulation with repulsion, Hooke spring attraction, and draggable nodes.
  - Traveling photon flux particles illustrating directional influence.
  - **Node radii and aura dynamically scaled to calculated centrality scores.**
- **Presets & Editor:**
  - Technology, Education, Space Agencies, Social Hierarchy, and Custom graph editor (add nodes, add directed links, delete edges).
- **"What If?" Live Topology Engine:**
  - Alter network structure (boost challenger or sever links from current leader) and watch real-time computed rank deltas ($\Delta \text{score}$ and $\Delta \text{rank}$).

---

### 3. 📐 NUMERICAL LAB (Academic Viva Suite)
- **Linear Systems ($A x = b$):** Step-by-step table comparing Jacobi vs Gauss-Seidel with spectral radius and error norms.
- **Bisection Root Finder:** Solving $f(x) = x^3 - 4x - 9 = 0$ on $[2, 3]$ with step-by-step bracket table $[a_k, b_k]$, midpoint $c_k$, and sign checks.
- **Newton-Raphson Solver:** Solving $f(x) = x^3 - 2x - 5 = 0$ showing quadratic convergence $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$.
- **Eigenvalues (Power Method):** Rayleigh quotient $\lambda^{(k)} = \frac{v^T A v}{v^T v}$ converging to dominant eigenvalue and eigenvector.

---

## 🎨 Design Philosophy & UX
- Cybernetic telemetry aesthetic inspired by mission control supercomputing terminals.
- Clean, non-intimidating interactive controls for everyday users.
- Deep mathematical transparency accessible on-demand via **"Show the Math"**, **"Compare Solvers"**, and **"Optimize Cooling"** modals.
