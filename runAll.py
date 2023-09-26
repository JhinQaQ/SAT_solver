import os
import sys

def run_solver_on_all_cnf_files(solver_script, directory='.'):
    # List all files in the specified directory
    files = os.listdir(directory)

    # Filter out files that don't end with .cnf
    cnf_files = [f for f in files if f.endswith('.cnf')]

    # Run the solver on each .cnf file
    for cnf_file in cnf_files:
        os.system(f"python {solver_script} {cnf_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_all.py <solver_script> [directory]")
    else:
        solver_script = sys.argv[1]
        directory = sys.argv[2] if len(sys.argv) > 2 else '.'
        run_solver_on_all_cnf_files(solver_script, directory)
