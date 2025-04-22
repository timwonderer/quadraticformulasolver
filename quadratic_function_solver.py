"""Quadratic Formula Solver Module

This module provides functionality to solve quadratic equations of the form ax^2 + bx + c = 0.
It depends on external modules to find integer square roots, simplify square roots, and reduce fractions.

The main function, quadratic_formula_by_parts, takes coefficients as input and computes the solutions by:
- Tracking parts of the quadratic formula in a dictionary with sign flags,
- Simplifying and reducing terms,
- Formatting and printing the final solutions.

"""

from integer_square_root_finder import findIntegerRoot
from square_root_simplifier import simplify_square_root
from reduce_fraction import parse_values
from answer_formatter import format_answer

def quadratic_formula_by_parts(coefficients):
  """Solve a quadratic equation using the quadratic formula, breaking down each part.

  Parameters:
    coefficients (dict): Dictionary with keys 'a', 'b', 'c' representing coefficients of ax^2 + bx + c = 0

  Returns:
    None

  Side-effects:
    Prints the solutions to the quadratic equation.
    Exits the program if 'a' is zero (not a quadratic equation).
  """
  # Extract coefficients a, b, c
  a = coefficients["a"]
  b = coefficients["b"]
  c = coefficients["c"]
  
  # Early guard: exit if a == 0 since the equation is not quadratic
  if a == 0:
    exit()
  
  two_a = 2 * a
  neg_b = -1 * b
  coefficient = None
  
  # Calculate the discriminant Δ = b^2 - 4ac
  discriminant = calculate_discriminant(a, b, c)
  radicand = discriminant
  
  # Initialize a dictionary to track values and their sign flags
  answer_tracker = {"neg_b":[neg_b, False], "coefficient":[coefficient, False], "two_a":[two_a, False],"radicand":[discriminant, False]}
  
  # Detect negative signs for each term and set flags accordingly
  for term, value in answer_tracker.items():
    if value[0] != None:
      if value[0] < 0:
        answer_tracker[term][1] = True
  
  # Handle discriminant cases:
  # If discriminant is not 0, ±1, simplify the square root
  if discriminant not in (0, 1, -1):
    discriminant = abs(discriminant)
    approx_root = findIntegerRoot(discriminant)
    coefficient, radicand = simplify_square_root(discriminant, approx_root)
  # If discriminant is ±1, set coefficient and radicand to 1
  elif discriminant in (1,-1):
    coefficient, radicand = 1, 1
  # If discriminant is 0, no radical part
  else:
    coefficient, radicand = 0, 0
  
  # Update the answer_tracker with new coefficient and radicand values
  answer_tracker["coefficient"][0] = coefficient
  answer_tracker["radicand"][0] = radicand
  
  # Build a dictionary of terms to be reduced (absolute values, ignoring radicand if 1)
  to_be_reduced = dict()
  for terms, values in answer_tracker.items():
    values[0] = abs(values[0])
    if terms != "radicand":
        if values[0] == 1:
          to_be_reduced[terms] = values
        else:
          continue
    else:
      continue
  
  # Reduce the terms using the parse_values function
  reduced_terms = parse_values(to_be_reduced)

  # Re-merge the reduced results back into answer_tracker
  answer_tracker.update(reduced_terms)

  
  # Format the final answers and print them
  return format_answer(answer_tracker)
 

def calculate_discriminant(a, b, c):
  """Calculate the discriminant of a quadratic equation.

  Parameters:
    a (int): Coefficient of x^2
    b (int): Coefficient of x
    c (int): Constant term

  Returns:
    int: The discriminant value b^2 - 4ac

  Side-effects:
    None
  """
  # Compute discriminant using formula b^2 - 4ac
  b_squared = b**2
  four_a_c = 4 * a * c
  discriminant = b_squared - four_a_c
  return (discriminant)
     
