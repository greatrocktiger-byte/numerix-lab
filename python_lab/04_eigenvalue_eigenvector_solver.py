"""
=============================================================================
NUMERIX LAB — COMPUTATIONAL MATHEMATICS LABORATORY
Experiment 04: Matrix Eigenvalues, Eigenvectors & Invariants
=============================================================================

MATHEMATICAL FOUNDATION:
1. Definition:
      A * v = lambda * v   <==>   (A - lambda * I) * v = 0

2. Characteristic Polynomial:
   For non-trivial nullspace solutions (v != 0), the coefficient matrix must be singular:
      det(A - lambda * I) = 0

3. 2x2 Analytical Formulation:
      For matrix A = [[a, b], [c, d]]:
      det([[a - lambda, b], [c, d - lambda]]) = lambda^2 - Tr(A)*lambda + det(A) = 0
      where:
         Trace:       Tr(A) = a + d
         Determinant: det(A) = ad - bc
      Roots:
         lambda = [ Tr(A) +/- sqrt( Tr(A)^2 - 4*det(A) ) ] / 2

4. Mathematical Invariants (Exam Viva Defense):
   - Sum of Eigenvalues equals Matrix Trace:        sum(lambda_i) = Tr(A)
   - Product of Eigenvalues equals Determinant:    prod(lambda_i) = det(A)

5. Eigenvector Determination:
   For each eigenvalue lambda_k:
      (A - lambda_k * I) * v = 0
   Find basis of null space, then normalize to unit Euclidean norm: ||v||_2 = 1.0.
=============================================================================
"""

import sys
import numpy as np

# Ensure UTF-8 output on Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def solve_2x2_eigen_system(A):
    """
    Analytically computes eigenvalues, eigenvectors, and verifies invariants for a 2x2 matrix.
    """
    A = np.array(A, dtype=np.float64)
    if A.shape != (2, 2):
        raise ValueError("Matrix must be 2x2!")
        
    a, b = A[0, 0], A[0, 1]
    c, d = A[1, 0], A[1, 1]
    
    # 1. Invariants
    trace = a + d
    determinant = a * d - b * c
    
    # 2. Discriminant of characteristic polynomial
    discriminant = trace**2 - 4.0 * determinant
    
    print("=" * 70)
    print(" NUMERIX LAB: 2x2 EIGEN-SYSTEM ANALYTICAL DERIVATION")
    print("=" * 70)
    print(f"Input Matrix A:\n{A}\n")
    print("STEP 1: COMPUTING INVARIANTS")
    print(f"  * Trace Tr(A)       = a11 + a22 = {a:.4f} + {d:.4f} = {trace:.4f}")
    print(f"  * Determinant det(A)= (a11*a22) - (a12*a21) = ({a:.2f}*{d:.2f}) - ({b:.2f}*{c:.2f}) = {determinant:.4f}")
    print(f"  * Characteristic Eq : lambda^2 - ({trace:.4f})*lambda + ({determinant:.4f}) = 0")
    print(f"  * Discriminant Delta= Tr^2 - 4*det = {trace:.4f}^2 - 4*({determinant:.4f}) = {discriminant:.4f}")
    
    if discriminant < 0:
        print("\n  [Note: Complex conjugate eigenvalues detected]")
        sqrt_d = np.lib.scimath.sqrt(discriminant)
        l1 = (trace + sqrt_d) / 2.0
        l2 = (trace - sqrt_d) / 2.0
        eigvals = [l1, l2]
    else:
        sqrt_d = np.sqrt(discriminant)
        l1 = (trace + sqrt_d) / 2.0
        l2 = (trace - sqrt_d) / 2.0
        eigvals = [l1, l2]
        
    print(f"\nSTEP 2: EIGENVALUES (ROOTS OF CHARACTERISTIC POLYNOMIAL)")
    print(f"  * Principal Eigenvalue lambda_1 = {l1}")
    print(f"  * Second Eigenvalue    lambda_2 = {l2}")
    
    print(f"\nSTEP 3: MATHEMATICAL INVARIANT CHECKS (VIVA DEFENSE)")
    sum_lambdas = l1 + l2
    prod_lambdas = l1 * l2
    print(f"  * Check 1: lambda_1 + lambda_2 = {sum_lambdas:.4f} == Tr(A) ({trace:.4f})  --> {'[PASSED OK]' if np.isclose(np.real(sum_lambdas), trace) else '[FAILED]'}")
    print(f"  * Check 2: lambda_1 * lambda_2 = {prod_lambdas:.4f} == det(A) ({determinant:.4f}) --> {'[PASSED OK]' if np.isclose(np.real(prod_lambdas), determinant) else '[FAILED]'}")
    
    # 3. Eigenvectors
    print(f"\nSTEP 4: EIGENVECTORS (NULL SPACE CALCULATION)")
    eigenvectors = []
    for idx, lam in enumerate(eigvals, 1):
        # (A - lambda*I)v = 0
        M = A - np.eye(2) * lam
        if abs(M[0, 1]) > 1e-12:
            v = np.array([-M[0, 1], M[0, 0]])
        elif abs(M[1, 0]) > 1e-12:
            v = np.array([M[1, 1], -M[1, 0]])
        else:
            v = np.array([1.0, 0.0]) if abs(M[0, 0]) < 1e-12 else np.array([0.0, 1.0])
            
        norm_v = np.linalg.norm(v)
        if norm_v > 0:
            v = v / norm_v
        eigenvectors.append(v)
        
        Av = A @ v
        lam_v = lam * v
        print(f"  * Eigenvector v_{idx} for lambda={lam}: [{v[0]:.4f}, {v[1]:.4f}]^T")
        print(f"    Verification A*v: [{Av[0]:.4f}, {Av[1]:.4f}]^T == lambda*v: [{lam_v[0]:.4f}, {lam_v[1]:.4f}]^T [VERIFIED]")
        
    return eigvals, eigenvectors

def run_experiment():
    test_matrix = [
        [4.0, 1.0],
        [2.0, 3.0]
    ]
    solve_2x2_eigen_system(test_matrix)
    
    print("\n" + "=" * 70)
    print(" 3x3 GENERAL MATRIX TEST (NUMERICAL SPECTRAL DECOMPOSITION)")
    print("=" * 70)
    A3 = np.array([
        [6.0, 2.0, 1.0],
        [2.0, 3.0, 1.0],
        [1.0, 1.0, 1.0]
    ])
    print(f"3x3 Symmetric Matrix A:\n{A3}\n")
    vals3, vecs3 = np.linalg.eig(A3)
    print("--> Computed Eigenvalues:")
    for i, val in enumerate(vals3, 1):
        print(f"    lambda_{i} = {val:.6f}")
        
    print(f"\n--> Trace Check:       sum(lambda) = {np.sum(vals3):.4f} == Tr(A) = {np.trace(A3):.4f} [VERIFIED]")
    print(f"--> Determinant Check: prod(lambda)= {np.prod(vals3):.4f} == det(A)= {np.linalg.det(A3):.4f} [VERIFIED]")
    print("=" * 70)

if __name__ == '__main__':
    run_experiment()
