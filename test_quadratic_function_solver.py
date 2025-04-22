from quadratic_function_solver import quadratic_formula_by_parts

cases = [
    {"a": 1, "b": -6, "c": 9},       # Perfect square trinomial
    {"a": 2, "b": 4, "c": 2},        # Discriminant = 0 (one real root)
    {"a": 1, "b": 1, "c": -2},       # Two distinct real roots
    {"a": 1, "b": 0, "c": -7},       # Missing b term
    {"a": 3, "b": -10, "c": 3},      # Two distinct real roots
    {"a": 2, "b": 3, "c": -5},       # Two distinct real roots
    {"a": 1, "b": 0, "c": 9},        # No real roots (complex roots)
    {"a": 0, "b": 2, "c": 1},        # Invalid case (a=0)
    {"a": 1, "b": 1, "c": -10001},   # Large discriminant
    {"a": -1, "b": -6, "c": -9},     # Negative leading coefficient
    {"a": 1, "b": -4, "c": 4},       # Perfect square trinomial
    {"a": 5, "b": 0, "c": -20},      # Missing b term
    {"a": 1, "b": 2, "c": 1},        # Discriminant = 0 (one real root)
    {"a": 1, "b": -1, "c": -6},      # Two distinct real roots
    {"a": 1, "b": 0, "c": 0},        # Root at origin
    {"a": 0, "b": 0, "c": 1},        # Invalid case (a=0, b=0)
    {"a": 1, "b": 1, "c": 1},        # No real roots (complex roots)
    {"a": -2, "b": 4, "c": -2},      # Perfect square trinomial
    {"a": 10, "b": -3, "c": 0},      # Missing c term
    {"a": 1, "b": -1000, "c": 1},    # Large b term
]

for i, coef in enumerate(cases, 1):
    try:
        print (coef)
        quadratic_formula_by_parts(coef)
    except SystemExit:
        print(f"Test {i}: {coef}  ->  Program exited (a=0 guard)")
