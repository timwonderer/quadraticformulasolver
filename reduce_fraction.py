def parse_values(terms):  # terms is a dict with entries like {'term': [value, is_neg]}
  if not terms:  # Same as if terms == dict() or if len(terms) == 0
    return terms

  reducible_terms = []
  for term, value in terms.items():
    mag = value[0]
    if term == "radicand":
      continue  # Skip radicand term
    elif mag > 1:  # Check if the term is reducible
      reducible_terms.append(value[0])

  if not reducible_terms:
    return terms  # No reducible terms found, return original terms

  common_factor = gcd(reducible_terms)  # Find the GCD of the non-zero terms

  for term, value in terms.items():
    if common_factor > 1:
      value[0] = value[0] // common_factor  # Reduce all the terms by the GCD

  return terms


def gcd(values):
  if len(values) == 0:
    return 0
  if len(values) == 1:
    return values[0]
  a = values[0]

  for i in range(1, len(values)):
    b = values[i]
    results = euclidean_algorithm(a, b)
    a = results

    if a == 1:
      break

  return a


def euclidean_algorithm(a, b):
  while b != 0:
    a, b = abs(b), abs(a % b)

  return a
