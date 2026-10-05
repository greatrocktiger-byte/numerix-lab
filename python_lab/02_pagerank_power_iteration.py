"""
=============================================================================
NUMERIX LAB — COMPUTATIONAL MATHEMATICS LABORATORY
Experiment 02: Spectral Graph Theory & PageRank (Power Iteration Method)
=============================================================================

MATHEMATICAL FOUNDATION:
1. Directed Network Graph: G = (V, E) with N nodes.
   Adjacency Matrix A: A_ij = 1 if directed edge j -> i exists, else 0.
   Out-Degree vector: d_j = sum_i(A_ij).

2. Column-Stochastic Transition Matrix M:
      M_ij = A_ij / d_j  ==>  sum_i(M_ij) = 1.0 for each column j.

3. The Google Matrix (Random Surfer Model with Damping Factor alpha = 0.85):
      G = alpha * M + [(1 - alpha) / N] * E
   where E is an N x N matrix of all ones (e * e^T).

4. Perron-Frobenius Theorem:
   Since G has strictly positive entries (G_ij > 0) and is column-stochastic:
   - The principal eigenvalue is exactly lambda_1 = 1.0.
   - The corresponding eigenvector r has strictly positive real entries.
   - The steady-state vector satisfies: G * r = 1.0 * r.

5. Power Iteration Algorithm:
   - Initialize r^(0) = [1/N, 1/N, ..., 1/N]^T
   - Iterative Step: r^(k+1) = G * r^(k)
   - Convergence Rate: Error decays as O(|lambda_2 / lambda_1|^k) = O(0.85^k).
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

def build_google_matrix(edges, num_nodes, alpha=0.85):
    """
    Constructs the column-stochastic transition matrix M and the Google Matrix G.
    edges: list of tuples (source_node, target_node) where indices are 0-based.
    """
    # 1. Adjacency Matrix
    A = np.zeros((num_nodes, num_nodes), dtype=np.float64)
    for u, v in edges:
        A[v, u] = 1.0  # Directed endorsement from u to v
        
    # 2. Transition Matrix M
    M = np.zeros((num_nodes, num_nodes), dtype=np.float64)
    out_degrees = np.sum(A, axis=0)
    
    for j in range(num_nodes):
        if out_degrees[j] > 0:
            M[:, j] = A[:, j] / out_degrees[j]
        else:
            # Dangling node (zero out-degree): distribute probability uniformly
            M[:, j] = 1.0 / num_nodes
            
    # 3. Google Matrix with Teleportation
    E = np.ones((num_nodes, num_nodes), dtype=np.float64)
    G = alpha * M + ((1.0 - alpha) / num_nodes) * E
    
    return M, G

def power_iteration(G, tol=1e-6, max_iters=100):
    """
    Executes Power Iteration to extract the dominant eigenvector corresponding to lambda_1 = 1.
    """
    N = G.shape[0]
    r = np.full(N, 1.0 / N, dtype=np.float64)
    
    history = [r.copy()]
    residuals = []
    
    for it in range(1, max_iters + 1):
        r_next = G @ r
        
        # Ensure L1 normalization (sum to 1)
        r_next /= np.sum(r_next)
        
        # Calculate L1 residual norm: ||r^(k+1) - r^(k)||_1
        diff = np.sum(np.abs(r_next - r))
        residuals.append(diff)
        history.append(r_next.copy())
        
        r = r_next
        if diff < tol:
            break
            
    return r, it, residuals, history

def run_experiment():
    print("=" * 70)
    print(" NUMERIX LAB: SPECTRAL GRAPH PAGERANK (POWER ITERATION ALGORITHM)")
    print("=" * 70)
    
    # Example 5-Node Academic Network
    # Nodes: 0: A (Server), 1: B (Database), 2: C (Client 1), 3: D (Client 2), 4: E (Gateway)
    node_names = ['Node A (Server)', 'Node B (Database)', 'Node C (Client 1)', 'Node D (Client 2)', 'Node E (Gateway)']
    N = len(node_names)
    
    # Directed Edges (from, to)
    edges = [
        (4, 0),  # Gateway -> Server
        (2, 0),  # Client 1 -> Server
        (3, 0),  # Client 2 -> Server
        (0, 1),  # Server -> Database
        (1, 0),  # Database -> Server
        (0, 4),  # Server -> Gateway
        (2, 1)   # Client 1 -> Database
    ]
    
    alpha = 0.85
    print(f"Network Size: {N} Nodes, {len(edges)} Directed Links")
    print(f"Damping Factor (alpha): {alpha}\n")
    
    M, G = build_google_matrix(edges, N, alpha)
    
    print("--> Column-Stochastic Transition Matrix M:")
    print(np.round(M, 3))
    print("\n--> Google Matrix G (M with alpha=0.85 teleportation):")
    print(np.round(G, 3))
    
    # Verify Perron-Frobenius conditions
    eigvals, eigvecs = np.linalg.eig(G)
    max_eig_idx = np.argmax(np.real(eigvals))
    print(f"\n--> True Principal Eigenvalue: lambda_1 = {np.real(eigvals[max_eig_idx]):.4f} (Expected: 1.0000)")
    
    # Run Power Iteration
    print("\n--> Starting Power Iteration sweeps...")
    r_final, iters, residuals, history = power_iteration(G)
    
    print(f"    Power Iteration Converged in {iters} steps!\n")
    print(f"{'Iteration':<10} | " + " | ".join([f"{name[:6]:<8}" for name in node_names]) + " | Residual L1")
    print("-" * 75)
    
    sample_steps = [0, 1, 2, 3, 5, min(10, iters), iters]
    for step in sorted(list(set(sample_steps))):
        vec = history[step]
        res_str = f"{residuals[step-1]:.2e}" if step > 0 else "Initial"
        vals_str = " | ".join([f"{val*100:6.2f}%" for val in vec])
        print(f"k = {step:<6} | {vals_str} | {res_str}")
        
    print("-" * 75)
    print("\n--> FINAL SPECTRAL AUTHORITY RANKINGS:")
    ranked_indices = np.argsort(r_final)[::-1]
    for rank, idx in enumerate(ranked_indices, 1):
        print(f"    Rank #{rank}: {node_names[idx]:<20} Score = {r_final[idx]:.4f} ({r_final[idx]*100:.2f}%)")
        
    # Plot Visual Bar Chart & Convergence Curve
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    fig.patch.set_facecolor('#0b0f19')
    
    # Subplot 1: PageRank Scores Bar Chart
    ax1.set_facecolor('#111827')
    colors = ['#38bdf8', '#34d399', '#f59e0b', '#a855f7', '#ec4899']
    bars = ax1.bar([name.split()[1] for name in node_names], r_final * 100, color=colors, edgecolor='#ffffff', lw=1, width=0.55)
    ax1.set_title('PageRank Stationary Distribution Vector (r*)', color='#f8fafc', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Probability Score (%)', color='#94a3b8')
    ax1.grid(True, linestyle=':', alpha=0.3, axis='y')
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval:.1f}%', ha='center', va='bottom', color='#f8fafc', fontweight='bold', fontsize=9)
        
    # Subplot 2: Power Iteration Error Decay
    ax2.set_facecolor('#111827')
    ax2.semilogy(range(1, len(residuals)+1), residuals, color='#38bdf8', marker='o', markersize=4, lw=2, label='Measured ||Δr||_1')
    # Theoretical decay line: C * alpha^k
    k_vals = np.arange(1, len(residuals)+1)
    decay_theory = residuals[0] * (alpha ** (k_vals - 1))
    ax2.semilogy(k_vals, decay_theory, color='#f59e0b', linestyle='--', lw=1.5, label='Theory O(α^k) Bound')
    ax2.set_title('Power Iteration Residual Decay Rate', color='#f8fafc', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Iteration Step (k)', color='#94a3b8')
    ax2.set_ylabel('Norm Residue ||r^(k+1) - r^(k)||_1', color='#94a3b8')
    ax2.grid(True, linestyle=':', alpha=0.3)
    ax2.legend(facecolor='#0f172a', edgecolor='#334155')
    
    plt.tight_layout()
    output_img = 'python_lab/pagerank_output.png'
    plt.savefig(output_img, dpi=200, facecolor=fig.get_facecolor())
    print(f"\n--> Saved visual plot: {output_img}")
    try:
        plt.show(block=False)
        plt.pause(0.5)
    except Exception:
        pass

if __name__ == '__main__':
    run_experiment()
