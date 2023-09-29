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
        if len(clause) == 1 and [-clause[0]] in clauses:
            return True
    return False


def is_satisfying(assignment, clauses):
    for clause in clauses:
        if not any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause):
            return False
    return True


def solve(num_vars, clauses):
    for i in range(2 ** num_vars):
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
        assignment = [(i + 1) if val else -(i + 1) for i, val in enumerate(result)]
        print(" ".join(map(str, assignment)))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python solver.py <filename>")
    else:
        main(sys.argv[1])
