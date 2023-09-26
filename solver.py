def read_dimacs(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

    num_vars = 0
    clauses = []

    for line in content:
        line = line.strip()
        if line.startswith('p'):
            _, _, num_vars, _ = line.split()
            num_vars = int(num_vars)
        elif not line.startswith('c') and line:
            clauses.append([int(x) for x in line.split()[:-1]])

    return num_vars, clauses

def check_conflicting_unit_clauses(clauses):
    for clause in clauses:
        # If the clause is a unit clause
        if len(clause) == 1:
            # Check for the negation of this clause in the list of clauses
            if [-clause[0]] in clauses:
                return True
    return False

def is_satisfying(assignment, clauses):
    for clause in clauses:
        if not any(lit if lit > 0 else not assignment[abs(lit)-1] for lit in clause):
            return False
    return True

def solve(num_vars, clauses):
    for i in range(2**num_vars):
        assignment = [(i & (1 << j)) != 0 for j in range(num_vars)]
        if is_satisfying(assignment, clauses):
            return assignment
    return None

def main(filename):
    num_vars, clauses = read_dimacs(filename)
    
    if check_conflicting_unit_clauses(clauses):
        print("UNSAT")
        return
    
    result = solve(num_vars, clauses)
    if result is None:
        print("UNSAT")
    else:
        assignment = []
        for i, val in enumerate(result, 1):
            assignment.append(i if val else -i)
        print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sat_solver.py <filename>")
    else:
        main(sys.argv[1])
    print('----------------------------------------------------')
