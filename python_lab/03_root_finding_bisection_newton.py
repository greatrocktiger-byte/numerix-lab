"""
=============================================================================
NUMERIX LAB — COMPUTATIONAL MATHEMATICS LABORATORY
Experiment 03: Non-Linear Root Finding (Bisection vs. Newton-Raphson)
=============================================================================

MATHEMATICAL FOUNDATION:
1. The Problem: Find root alpha such that f(alpha) = 0.

2. Bisection Method (Bracketing / Closed Domain):
   - Theoretical Basis: Intermediate Value Theorem (IVT).
     If f(x) is continuous on [a, b] and f(a) * f(b) < 0, a root exists in (a, b).
   - Update Equation: Midpoint c = (a + b) / 2.
     Replace bracket: if f(a)*f(c) < 0 then b = c, else a = c.
   - Order of Convergence: Linear (p = 1).
     Error bound after n iterations: epsilon_n = (b - a) / (2^n).
   - Guarantee: 100% unconditional convergence.

3. Newton-Raphson Method (Open Domain / Tangent Line):
   - Theoretical Basis: First-order Taylor series approximation:
     f(x_{n+1}) approx f(x_n) + f'(x_n) * (x_{n+1} - x_n) = 0
   - Update Equation:
     x_{n+1} = x_n - [ f(x_n) / f'(x_n) ]
   - Order of Convergence: Quadratic (p = 2).
     Error relation: epsilon_{n+1} approx C * (epsilon_n)^2.
     Doubles the number of accurate decimal places at every single step!
   - Failure Modes: Division by zero when f'(x_n) approx 0, local oscillation cycles.
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt

# Example Non-linear Function: f(x) = x^3 - 2*x - 5 = 0 (Famous historical root problem)
# Root is approximately x ≈ 2.09455148
def f(x):
    return x**3 - 2.0*x - 5.0

def df(x):
    return 3.0*(x**2) - 2.0

def bisection_method(f_func, a, b, tol=1e-6, max_iters=100):
    """
    Executes Bisection Method on [a, b].
    """
    fa, fb = f_func(a), f_func(b)
    if fa * fb >= 0:
        raise ValueError(f"IVT condition violated: f(a)={fa:.3f} and f(b)={fb:.3f} have identical signs!")
        
    history = []
    print(f"{'Step':<5} | {'a':<10} | {'b':<10} | {'Midpoint (c)':<12} | {'f(c)':<12} | {'Interval Width'}")
    print("-" * 70)
    
    for it in range(1, max_iters + 1):
        c = (a + b) / 2.0
        fc = f_func(c)
        width = abs(b - a)
        history.append({'iter': it, 'x': c, 'fx': fc, 'error': width / 2.0})
        
        print(f"{it:<5} | {a:<10.6f} | {b:<10.6f} | {c:<12.6f} | {fc:<12.2e} | {width:<10.6f}")
        
        if abs(fc) < tol or (width / 2.0) < tol:
            break
            
        if f_func(a) * fc < 0:
            b = c
        else:
            a = c
            
    return c, it, history

def newton_raphson_method(f_func, df_func, x0, tol=1e-6, max_iters=100):
    """
    Executes Newton-Raphson Method starting from x0.
    """
    x = x0
    history = []
    print(f"{'Step':<5} | {'x_n':<12} | {'f(x_n)':<14} | {'f\'(x_n)':<12} | {'Step Size |dx|'}")
    print("-" * 65)
    
    for it in range(1, max_iters + 1):
        fx = f_func(x)
        dfx = df_func(x)
        
        if abs(dfx) < 1e-12:
            raise ZeroDivisionError(f"Newton-Raphson failed: Derivative f'({x}) is zero!")
            
        x_next = x - (fx / dfx)
        step_size = abs(x_next - x)
        history.append({'iter': it, 'x': x_next, 'fx': f_func(x_next), 'error': step_size})
        
        print(f"{it:<5} | {x:<12.6f} | {fx:<14.2e} | {dfx:<12.4f} | {step_size:<10.2e}")
        
        x = x_next
        if step_size < tol or abs(f_func(x)) < tol:
            break
            
    return x, it, history

def run_experiment():
    print("=" * 70)
    print(" NUMERIX LAB: NON-LINEAR ROOT FINDING EXPERIMENT")
    print(" Target Function: f(x) = x^3 - 2x - 5 = 0")
    print("=" * 70)
    
    tol = 1e-6
    
    # 1. Run Bisection
    print("\n--> 1. EXECUTING BISECTION METHOD on Interval [2.0, 3.0]:")
    root_bis, iters_bis, hist_bis = bisection_method(f, 2.0, 3.0, tol=tol)
    print(f"    Bisection converged to Root = {root_bis:.8f} in {iters_bis} iterations.\n")
    
    # 2. Run Newton-Raphson
    print("--> 2. EXECUTING NEWTON-RAPHSON METHOD with Initial Guess x0 = 3.0:")
    root_nr, iters_nr, hist_nr = newton_raphson_method(f, df, 3.0, tol=tol)
    print(f"    Newton-Raphson converged to Root = {root_nr:.8f} in {iters_nr} iterations.\n")
    
    # Theoretical Comparison
    print("=" * 70)
    print(" MATHEMATICAL COMPARISON SUMMARY:")
    print(f"   Bisection Iterations:      {iters_bis:<3} (Linear O(1/2^n) Halving)")
    print(f"   Newton-Raphson Iterations: {iters_nr:<3} (Quadratic O(eps^2) Speed)")
    print(f"   Speedup Factor:            {iters_bis / iters_nr:.1f}x fewer steps for Newton-Raphson!")
    print("=" * 70)
    
    # Plot Visual Curve and Convergence comparison
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.patch.set_facecolor('#0b0f19')
    
    # Subplot 1: Function Curve and Root
    ax1.set_facecolor('#111827')
    xs = np.linspace(1.5, 3.2, 200)
    ys = f(xs)
    ax1.plot(xs, ys, color='#38bdf8', lw=2.5, label='f(x) = x^3 - 2x - 5')
    ax1.axhline(0, color='#64748b', linestyle='--', lw=1)
    ax1.scatter([root_nr], [0], color='#10b981', s=120, zorder=5, label=f'Root alpha approx {root_nr:.4f}')
    
    # Plot initial Newton tangent line
    x0 = 3.0
    y0 = f(x0)
    slope = df(x0)
    x_tan = np.linspace(2.0, 3.2, 50)
    y_tan = slope * (x_tan - x0) + y0
    ax1.plot(x_tan, y_tan, color='#f43f5e', linestyle=':', lw=1.5, label='Tangent at x₀=3.0')
    ax1.set_title('Function Geometry & Tangent Projection', color='#f8fafc', fontsize=11, fontweight='bold')
    ax1.set_xlabel('x', color='#94a3b8')
    ax1.set_ylabel('f(x)', color='#94a3b8')
    ax1.grid(True, linestyle=':', alpha=0.3)
    ax1.legend(facecolor='#0f172a', edgecolor='#334155')
    
    # Subplot 2: Convergence Rates (Error vs Iteration)
    ax2.set_facecolor('#111827')
    errs_bis = [h['error'] for h in hist_bis]
    errs_nr = [h['error'] for h in hist_nr]
    ax2.semilogy(range(1, len(errs_bis)+1), errs_bis, color='#38bdf8', marker='o', lw=2, label=f'Bisection (p=1, {iters_bis} iters)')
    ax2.semilogy(range(1, len(errs_nr)+1), errs_nr, color='#34d399', marker='s', lw=2, label=f'Newton-Raphson (p=2, {iters_nr} iters)')
    ax2.axhline(tol, color='#f59e0b', linestyle='--', label=f'Tolerance ({tol})', lw=1.5)
    ax2.set_title('Log-Error Decay: Linear vs Quadratic Order', color='#f8fafc', fontsize=11, fontweight='bold')
    ax2.set_xlabel('Iteration Number', color='#94a3b8')
    ax2.set_ylabel('Absolute Error |x_n - Root|', color='#94a3b8')
    ax2.grid(True, linestyle=':', alpha=0.3)
    ax2.legend(facecolor='#0f172a', edgecolor='#334155')
    
    plt.tight_layout()
    output_img = 'python_lab/root_finding_output.png'
    plt.savefig(output_img, dpi=200, facecolor=fig.get_facecolor())
    print(f"\n--> Saved visual plot: {output_img}")
    try:
        plt.show(block=False)
        plt.pause(0.5)
    except Exception:
        pass

if __name__ == '__main__':
    run_experiment()
