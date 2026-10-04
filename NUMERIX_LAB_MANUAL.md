# NUMERIX LAB — Comprehensive Project Guide & User Manual

> **Product Name:** NUMERIX LAB  
> **Tagline:** *Numerical Methods, Visualized.*  
> **Project Scope:** Computational Mathematics & Numerical Simulation Platform  
> **Access URL:** `http://localhost:3000` (Runs locally in any modern web browser)  
> **Author:** Antigravity AI & greatrocktiger-byte

---

## 1. Executive Summary: What is NUMERIX LAB?

In traditional university mathematics and engineering curricula, **Numerical Methods** (such as Jacobi iteration, Gauss-Seidel, Bisection root finding, Newton-Raphson tangents, and Eigenvalues) are taught as abstract pencil-and-paper equations or boring command-line printouts. Students often memorize formulas without understanding how heat actually diffuses across a silicon die, or how Google calculates the ranking of the world wide web using an eigenvector.

**NUMERIX LAB** bridges this gap. It turns mathematical formulations into a **futuristic, interactive, real-time computational simulation laboratory**.

### 🌟 Core Design Philosophy:
- **100% Real Mathematics:** Nothing is faked or decorative. Heatmaps, error residuals, matrix transformations, and network graphs are computed on the fly using verified numerical algorithms.
- **Zero-Friction Visualization:** Discrete mathematical grids are translated into continuous infrared FLIR heatmaps, interactive physics network graphs, and step-by-step convergence curves.
- **Viva & Presentation Ready:** Every module contains explicit explanations, mathematical formulas, and step-by-step playback controls designed specifically for academic viva examiners.

---

## 2. Architecture & The 3 Flagship Experiences

NUMERIX LAB is divided into three distinct modules accessible via the top navigation bar or the home screen:

```
                          NUMERIX LAB
              ("Numerical Methods, Visualized.")
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
   THERMALX            LINKRANK          NUMERICAL LAB
(2D Heat Diffusion) (Network Centrality) (Viva Solver Suite)
```

---

### Module 1: THERMALX — Thermal Field Simulation & Optimization

#### What is it?
THERMALX simulates the thermodynamic temperature distribution over a 2D computational motherboard/chassis (such as a modern gaming laptop or server blade) containing discrete heat sources (CPU, GPU, Battery) and active cooling sinks.

#### The Underlying Mathematics:
It solves the steady-state **2D Poisson/Laplace Heat Conduction Equation with Convective Cooling**:
$$k \nabla^2 T(x, y) + Q(x, y) - h_{\text{conv}} \cdot (T(x, y) - T_{\text{amb}}) = 0$$

Using a 5-point finite-difference stencil on a discrete $(N \times M)$ grid:
$$T_{i, j}^{(k+1)} = \frac{T_{i+1, j} + T_{i-1, j} + T_{i, j+1} + T_{i, j-1} + \frac{\Delta x^2}{k} Q_{i,j} + \frac{h \Delta x^2}{k} T_{\text{amb}}}{4 + \frac{h \Delta x^2}{k}}$$

#### Key Features in THERMALX:
1. **Pre-built Laptop Simulation:** Allows configuring ambient temperature, CPU die heat (e.g. 85°C), GPU die heat (e.g. 75°C), battery heat (40°C), cooling fan intensity, and grid resolution.
2. **Dual Numerical Solvers (Jacobi vs. Gauss-Seidel):**
   - **Jacobi Method:** Computes the entire next grid from the previous iteration $k$ without immediately reusing new values.
   - **Gauss-Seidel Method:** Immediately reuses freshly computed neighboring values within the same iteration step, achieving a **~2x to 3x convergence speedup**.
3. **Cooling Optimization via Bisection Method:** Solves an inverse engineering problem: *"What exact cooling fan percentage is needed to keep the peak chassis temperature strictly under 75°C?"* Uses genuine Bisection bracket halving.
4. **Custom Grid CAD Designer:** An interactive sandbox where you can paint custom heat injectors, cooling sinks, and zero-flux insulators on a 16x16 computational matrix.
5. **Thermal Challenges:** Scored gamified missions (e.g., thermal throttling stabilization under heavy computational load).

---

### Module 2: LINKRANK — Network Graph Centrality & Eigenvalues

#### What is it?
LINKRANK models how information, authority, and ranking flow across interconnected networks (such as web pages, citation graphs, social networks, or neural pathways). It explains the fundamental algorithm behind Google's PageRank.

#### The Underlying Mathematics:
1. **Column-Stochastic Transition Matrix ($M$):**
   $$M_{ij} = \begin{cases} \frac{1}{\text{deg}(j)} & \text{if link } j \to i \text{ exists} \\ 0 & \text{otherwise} \end{cases}$$
2. **Google Matrix with Random Surfer Damping ($d = 0.85$):**
   $$G = d \cdot M + \frac{1 - d}{N} \cdot \mathbf{E}$$
3. **Perron-Frobenius Dominant Eigenvalue ($\lambda_1 = 1.000$):**
   Using the **Power Iteration Method**:
   $$v^{(k+1)} = \frac{G \cdot v^{(k)}}{\|G \cdot v^{(k)}\|_1}$$
   As $k \to \infty$, $v^{(k)}$ converges to the unique stationary probability distribution vector.

#### Key Features in LINKRANK:
1. **Real-Time Force-Directed Physics Graph:** Interactive nodes and links where node diameters and glowing aura pulses dynamically scale to their computed eigenvector centrality score.
2. **Live "What-If" Topology Perturbation Engine:**
   - **Boost Challenger:** Dynamically redirects inbound hyperlinks to a low-ranked node and recalculates power iterations live to show rank elevation.
   - **Dethrone Leader:** Sever incoming links from the highest authority node to witness rank collapse across the network.
3. **Network Topology Editor:** Add custom nodes, create directed links, adjust damping factors, and observe matrix updates in real time.

---

### Module 3: NUMERICAL LAB — Academic Viva & Exam Suite

#### What is it?
A dedicated interactive demonstration suite built specifically for syllabus verification, professor inspections, and oral viva exams.

#### The 4 Interactive Solvers:
1. **Linear Systems ($Ax = b$) — Jacobi vs. Gauss-Seidel:**
   - Compares convergence on strictly diagonally dominant and weakly dominant systems.
   - **Live Logarithmic Convergence Canvas:** Dynamically plots $\log_{10}(\text{Error})$ vs Iteration $k$ comparing Jacobi (Cyan) vs Gauss-Seidel (Orange).
   - **Animated Step-by-Step Player:** Walk through row by row with audio feedback.
2. **Bisection Method Root Finder ($f(x) = 0$):**
   - Solves polynomial, transcendental, and radiation equations:
     - $f(x) = x^3 - 4x - 9 = 0$
     - $f(x) = \cos(x) - x = 0$ (Dottie transcendental root)
     - $f(T) = T^4 - 2.5 \times 10^7 = 0$ (Stefan-Boltzmann radiation)
   - **Real-Time Bracket Validator:** Checks if $f(a) \cdot f(b) \le 0$ as you type.
   - **Live Canvas Visualization:** Shows the curve $f(x)$, zero-axis, active brackets $[a_k, b_k]$, and midpoint $c_k$ zooming into the root.
3. **Newton-Raphson Nonlinear Solver:**
   - Demonstrates quadratic convergence ($\varepsilon_{k+1} \propto \varepsilon_k^2$, doubling precision digits each step):
     $$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$$
   - **Live Tangent Canvas:** Illustrates the tangent line from $(x_k, f(x_k))$ projecting down to the $x$-intercept $(x_{k+1}, 0)$.
4. **Power Iteration Method (Dominant Eigenvalues):**
   - Computes the dominant eigenvalue $\lambda_1$ and principal eigenvector $v_1$ using Rayleigh quotient estimates:
     $$\lambda^{(k)} = \frac{v^T A v}{v^T v}$$
   - **Live Rayleigh Canvas & Component Gauges:** Displays the asymptotic curve of $\lambda^{(k)}$ alongside animated coordinate bars.

---

## 3. Real-World Use Cases (Why does this matter?)

| Domain | Real-World Application | How NUMERIX LAB Demonstrates It |
| :--- | :--- | :--- |
| **Electronics & Hardware** | Laptop, smartphone, and GPU thermal throttling & heatsink placement | **THERMALX** shows how heat from high-dissipation silicon dies diffuses to the chassis edges and computes exact fan RPM needed. |
| **Search Engines & Social Media** | Web ranking (Google PageRank), Twitter influence, research paper citations | **LINKRANK** calculates eigenvector centrality via power iterations and tests how linking patterns boost or demote authority. |
| **Mechanical & Aerospace** | Structural finite-element analysis (FEA), fluid dynamics | Demonstrates how large sparse linear matrices ($Ax = b$) are solved iteratively using Jacobi and Gauss-Seidel methods. |
| **Quantitative Finance & Data** | Yield curve root solving, implied volatility extraction, PCA (Principal Component Analysis) | **NUMERICAL LAB** uses Bisection, Newton-Raphson, and Power Iteration to solve non-linear roots and matrix eigenvalues. |

---

## 4. Step-by-Step User Guide (How to Run and Demo)

### Step 1: Open the Application
1. Ensure the project server is running locally (e.g., `python -m http.server 3000`).
2. Open Google Chrome, Firefox, or Edge and visit:
   👉 **`http://localhost:3000`**

---

### Step 2: Test the Universal Navigation & Breadcrumbs
- Notice the **Universal Navigation Bar** right below the header:
  - `← BACK` button: Remembers your navigation path and cleanly backtracks to the previous screen.
  - **Interactive Breadcrumb Trail:** E.g., `Home / THERMALX / Laptop Simulation / Simulation Results`. You can click any parent breadcrumb to jump directly to it.
  - **Quick Jump Module Pills:** Directly switch between `🔥 ThermalX`, `🕸️ LinkRank`, and `🧮 Numerical Lab`.

---

### Step 3: Run THERMALX (Laptop Thermal Simulation)
1. On the Home page, click **`Get Started ->`** or the **`Laptop Simulation`** card.
2. On the configuration screen, tweak any parameters (or leave the realistic defaults):
   - CPU Die: `85°C`
   - GPU Die: `75°C`
   - Battery: `40°C`
   - Cooling Convection: `45%`
   - Method: Select **Gauss-Seidel** (default) or **Jacobi**.
3. Click **`Run Simulation`**.
4. Watch the live **Thermal Engine Initializer** step through grid boundaries and iterate.
5. On the **Simulation Results** screen:
   - Hover your mouse across the heatmap to inspect live localized temperatures.
   - Look at the **Vertical Thermal Scale (100°C to 25°C)** on the right: a white level indicator pip follows your cursor in real time.
   - Click **`Smoothing: High (FLIR)`** at the bottom to toggle between continuous infrared camera mode and raw discrete finite-difference CAD mesh!
   - Click **`Compare Solvers`** to see Jacobi vs Gauss-Seidel convergence side-by-side with an error plot.
   - Click **`Optimize Cooling (Bisection)`** to see the system automatically solve for the minimum fan percentage required to stay below 75°C.
   - Click **`Show the Math`** to review the governing Poisson equations.
   - Click **`Lab Report`** in the top bar to download an official formatted `.txt` simulation report!

---

### Step 4: Explore LINKRANK (Network Influence Engine)
1. Click **`LINKRANK`** in the top header or Home page.
2. Click **`Explore Network`** and select a preset (e.g. `Tech Web Graph` or `Corporate Hierarchy`).
3. Click **`Calculate Ranking`**:
   - Watch the Power Iteration algorithm compute dominant eigenvectors.
   - Nodes expand in size proportionally to their computed authority.
4. Click **`What If? (Live Topology Changes)`**:
   - Click **`Boost Challenger`**: Inbound links are rerouted; watch how the challenger node jumps up in ranking!
   - Click **`Dethrone Leader`**: Inbound links are cut; watch how the former leader plummets down the leaderboard.

---

### Step 5: Master the NUMERICAL LAB (Viva Center)
1. Click **`NUMERICAL LAB`** in the top header or the **`Numerical Viva Lab`** card on the home page.
2. Select any tab:
   - **Tab 1: Jacobi vs Gauss-Seidel**: Select a preset, then click **`▶ Run Solver Animated`**. Watch the table populate row by row with audio ticks and see the dual convergence curve draw live!
   - **Tab 2: Bisection Method**: Pick a function, change $a$ or $b$, observe the live `✓ Valid Bracket` validation, and click **`▶ Run Bisection Animated`** to watch the bracket lines shrink toward the root on the canvas.
   - **Tab 3: Newton-Raphson**: Enter an initial guess $x_0$, click **`▶ Run Newton Animated`**, and observe the tangent line projection pinpointing the root in 4 rapid steps!
   - **Tab 4: Power Method**: Choose a matrix preset, click **`Compute Dominant λ₁`**, and observe the Rayleigh quotient leveling off as normalized vector coordinate bars update live.

---

## 5. Viva / Presentation Q&A (Examiner Cheat Sheet)

When presenting this project to an examiner or professor, here are the top questions they will ask and how this application proves the answers:

#### Q1: "Why does Gauss-Seidel converge faster than Jacobi iteration?"
> **Answer:**  
> "In the Jacobi method, updating cell $(i, j)$ at step $(k+1)$ uses only values from the previous step $k$. In Gauss-Seidel, as soon as a cell value is updated, it is immediately reused in the calculation of the neighboring cells within the *same* iteration. This effectively squares the spectral radius of the iteration matrix ($\rho(T_{GS}) \approx \rho(T_J)^2$), which NUMERIX LAB demonstrates by showing Gauss-Seidel converging in roughly half the iterations of Jacobi."

#### Q2: "What is the convergence rate of Bisection vs Newton-Raphson?"
> **Answer:**  
> - "The **Bisection method** has **linear convergence** with an error reduction factor of exactly $0.5$ ($\varepsilon_{k+1} = 0.5 \cdot \varepsilon_k$). It is slow but unconditionally guaranteed to converge by the Intermediate Value Theorem as long as $f(a) \cdot f(b) \le 0$."  
> - "**Newton-Raphson** has **quadratic convergence** ($\varepsilon_{k+1} \propto \varepsilon_k^2$). The number of correct decimal places doubles with each iteration, converging in just 4 to 5 steps, as visualized on our tangent line canvas."

#### Q3: "How does the Power Method connect to Google PageRank?"
> **Answer:**  
> "The web graph is represented as a column-stochastic probability transition matrix $M$. Adding a damping factor ($d = 0.85$) produces the irreducible, primitive Google matrix $G$. By the **Perron-Frobenius theorem**, this matrix has a unique dominant eigenvalue $\lambda_1 = 1.000$. Repeated matrix-vector multiplications via the Power Iteration Method ($v^{(k+1)} = G v^{(k)}$) isolate the principal eigenvector, which represents the steady-state probability of a user visiting each webpage—this is PageRank."

#### Q4: "Is this simulation using real physics or pre-recorded animations?"
> **Answer:**  
> "It uses genuine numerical calculations. In THERMALX, every iteration updates a 2D matrix using finite-difference Laplacian stencils until the maximum residual error drops below the user-specified tolerance ($10^{-4}$). In LINKRANK and Numerical Lab, all numbers in the tables and canvas plots are calculated dynamically from user inputs using pure mathematical algorithms."

---
*Created for NUMERIX LAB — Computational Mathematics Academic Showcase.*
