"""
=============================================================================
NUMERIX LAB — MASTER COMPUTATIONAL MATHEMATICS RUNNER
A unified terminal interface to execute all university lab experiments.
=============================================================================
"""

import os
import sys
import subprocess

SCRIPTS = {
    '1': ('2D Thermal Conduction (Jacobi vs Gauss-Seidel)', '01_thermal_solver.py'),
    '2': ('PageRank & Power Iteration (Spectral Graph Theory)', '02_pagerank_power_iteration.py'),
    '3': ('Non-Linear Root Finding (Bisection vs Newton-Raphson)', '03_root_finding_bisection_newton.py'),
    '4': ('Eigenvalues, Eigenvectors & Invariants Verification', '04_eigenvalue_eigenvector_solver.py')
}

def print_banner():
    print("\n" + "=" * 76)
    print("      _   _ _   _ __  __ _____ ____  ______   __  _        _    ____  ")
    print("     | \\ | | | | |  \\/  | ____|  _ \\|_ _|\\ \\ / / | |      / \\  | __ ) ")
    print("     |  \\| | | | | |\\/| |  _| | |_) || |  \\ V /  | |     / _ \\ |  _ \\ ")
    print("     | |\\  | |_| | |  | | |___|  _ < | |   | |   | |___ / ___ \\| |_) |")
    print("     |_| \\_|\\___/|_|  |_|_____|_| \\_\\___|  |_|   |_____/_/   \\_\\____/ ")
    print("              COMPUTATIONAL MATHEMATICS LABORATORY SUITE               ")
    print("=" * 76)

def run_script(filename):
    script_path = os.path.join(os.path.dirname(__file__), filename)
    print(f"\n[EXECUTING] python {filename} ...\n")
    subprocess.run([sys.executable, script_path])

def main():
    while True:
        print_banner()
        print(" SELECT AN EXPERIMENT TO EXECUTE FOR SIR / EXAMINER:\n")
        for key, (name, _) in SCRIPTS.items():
            print(f"   [{key}] {name}")
        print("   [5] Run All 4 Experiments Sequentially")
        print("   [0] Exit")
        print("-" * 76)
        
        choice = input(" Enter option (0-5): ").strip()
        if choice == '0':
            print("\nExiting Numerix Lab Runner. Good luck with your Viva!\n")
            break
        elif choice in SCRIPTS:
            run_script(SCRIPTS[choice][1])
            input("\n[Press ENTER to return to menu...]")
        elif choice == '5':
            for k in sorted(SCRIPTS.keys()):
                run_script(SCRIPTS[k][1])
                print("\n" + "-" * 76)
            input("\n[All experiments completed. Press ENTER to return to menu...]")
        else:
            print("\nInvalid choice. Please select 0 to 5.")

if __name__ == '__main__':
    main()
