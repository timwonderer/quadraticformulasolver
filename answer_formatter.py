from reduce_fraction import gcd

def format_answer(terms_dict):
    """Format the quadratic formula components into readable solutions.

    Parameters:
        terms_dict (dict): Dictionary containing parts of the quadratic formula with sign flags.

    Returns:
        list of str: Formatted solution strings.

    Side-effects:
        None.
    """
    # Apply negative signs based on flags
    for terms, values in terms_dict.items():
        if values[1]:
            values[0] *= -1

    solutions = []
    neg_b = terms_dict["neg_b"][0]
    coefficient = terms_dict["coefficient"][0]
    two_a = terms_dict["two_a"][0]
    radicand = terms_dict["radicand"][0]

    if coefficient == 0 or radicand == 0:
        solutions = one_solution(solutions, neg_b, two_a)
    else:
        solutions = two_solutions(solutions, neg_b, coefficient, two_a, radicand)

    return solutions


def one_solution(solutions, neg_b, two_a):
    # Single root or no radical solution (discriminant zero or no radical part)
    if neg_b == 0:  # Solution is zero
        solution = str(0)
        solutions.append(solution)
        return solutions

    elif neg_b % two_a == 0:  # One solution with no fraction
        solution = str(neg_b // two_a)
        solutions.append(solution)
        return solutions

    else:  # One solution with a fraction
        top = abs(neg_b)
        bottom = abs(two_a)
        if neg_b / two_a < 0:
            top *= -1
        solution = f"{neg_b}/{two_a}"
        solutions.append(solution)
        return solutions


def two_solutions(solutions, neg_b, coefficient, two_a, radicand):
    if radicand == 1 or radicand == -1:
        top1 = neg_b + coefficient
        top2 = neg_b - coefficient
        imaginary = "i" if radicand == -1 else ""

        common_factor1 = gcd([abs(top1), abs(two_a)])
        common_factor2 = gcd([abs(top2), abs(two_a)])
        top1, two_a_1 = top1 // common_factor1, two_a // common_factor1
        top2, two_a_2 = top2 // common_factor2, two_a // common_factor2

        if top1 / two_a_1 < 0:  # Check if the first solution is negative
            top1 = -1 * abs(top1)
            two_a_1 = abs(two_a_1)
        if top2 / two_a_2 < 0:  # Check if the second solution is negative
            top2 = -1 * abs(top2)
            two_a_2 = abs(two_a_2)

        if top1 % two_a_1 == 0:  # Check if the first solution has no fraction
            bottom1 = ""
            top1 = top1 // two_a_1
            fraction1 = ""
        else:
            bottom1 = str(two_a_1)
            fraction1 = "/"
        if top2 % two_a_2 == 0:  # Check if the second solution has no fraction
            bottom2 = ""
            top2 = top2 // two_a_2
            fraction2 = ""
        else:
            bottom2 = two_a_2
            fraction2 = "/"

        solution1 = f"{top1}{imaginary}{fraction1}{bottom1}"
        solution2 = f"{top2}{imaginary}{fraction2}{bottom2}"
        solutions.extend([solution1, solution2])
        return solutions

    # Two solutions with radical sign (general case)
    elif coefficient != 0 and radicand not in (1, -1, 0):
        imaginary = "i" if radicand < 0 else ""
        radical = f"√{abs(radicand)}"

        common_factor = gcd([abs(neg_b), abs(coefficient), abs(two_a)])
        neg_b, coefficient, two_a = (
            neg_b // common_factor,
            coefficient // common_factor,
            two_a // common_factor,
        )

        if neg_b == 0:
            solution1 = ""
            solution2 = ""
        else:
            solution1 = neg_b
            solution2 = neg_b

        if coefficient == 1:
            coefficient = ""
        if neg_b / two_a < 0:
            neg_b = -1 * abs(neg_b)
            bottom = abs(two_a)
        else:
            neg_b, bottom = abs(neg_b), abs(two_a)

        if two_a in (1, -1):
            fraction = ""
            bottom = ""
        else:
            fraction = "/"

        top1 = f"{solution1}+{coefficient}{radical}{imaginary}"
        bottom1 = f"{fraction}{bottom}"
        top2 = f"{solution2}-{coefficient}{radical}{imaginary}"
        bottom2 = f"{fraction}{bottom}"

        if top1[0] == "+":
            top1 = top1[1:]
        if top2[0] == "+":
            top2 = top2[1:]

        solution1 = f"{top1}{bottom1}"
        solution2 = f"{top2}{bottom2}"
        if bottom1 != "":
            solution1 = f"({top1}){bottom1}"
        if bottom2 != "":
            solution2 = f"({top2}){bottom2}"

        solutions.extend([solution1, solution2])
        return solutions
