def sieve_of_eratosthenes(limit):
    """Return {prime: 0, ...} for every prime ≤ limit."""
    # Boolean sieve
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    # Build dict of primes → exponent 0
    return {p: 0 for p, is_prime in enumerate(sieve) if is_prime}


def divisible_by_two(n, factors):
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    return n, factors

    
def divisible_by_five(n, factors):
    if n < 5 or 5 not in factors:
        return n, factors
    while n % 5 == 0:
        factors[5] += 1
        n //= 5
    return n, factors


def divisible_by_three(num, prime_factors):
    if num < 3:
      return (num, prime_factors)
    divisible_by_three_test = 0
    for digit in str(num):
        divisible_by_three_test += int(digit)
    if divisible_by_three_test % 3 == 0:
        prime_factors[3] += 1
        i = 2
        while num % (3**i) == 0:
            prime_factors[3] += 1
            i += 1
        num = num // (3 ** prime_factors[3])
        return (num, prime_factors)
    else:
        return (num, prime_factors)

def divisible_by_eleven(num, prime_factors):
  if num < 11:
    return (num, prime_factors)
  elif 11 not in prime_factors:
    return (num, prime_factors)
  else:
    divisible_by_eleven_test = 0
    digit_list = list(str(num))
    count = 0
    # Calculate alternating sum: add then subtract digits.
    for digit in digit_list:
        if count == 0:
            divisible_by_eleven_test = int(digit)
        elif count % 2 != 0:
            divisible_by_eleven_test -= int(digit)
        elif count % 2 == 0:
            divisible_by_eleven_test += int(digit)
        count += 1
        
    if divisible_by_eleven_test % 11 == 0:
        prime_factors[11] = 1
        i = 2
        while num % (11**i) == 0:
            prime_factors[11] += 1
            i += 1
        num = num // (11 ** prime_factors[11])
        return (num, prime_factors)
    else:
        return (num, prime_factors)
    
def prime_division_test(n, prime_to_test, factors):
    if n % prime_to_test == 0:
        while n % prime_to_test == 0:
            factors[prime_to_test]+= 1
            n = n // prime_to_test
    return (n, factors)

def factorization_controller(num, prime_factors):
  num, prime_factors = divisible_by_two(num, prime_factors)
  num, prime_factors = divisible_by_three(num, prime_factors)
  num, prime_factors = divisible_by_five(num, prime_factors)
  num, prime_factors = divisible_by_eleven(num, prime_factors)
    
    # Iterate through the dictionary to test remaining primes.
  for prime in sorted(prime_factors):
      if prime > num:                      # nothing bigger can divide num
          break
  
      if prime_factors[prime] == 0:        # we haven’t used this prime yet
          if prime == num:                 # num itself is prime
              prime_factors[prime] += 1
              num //= prime
          elif prime < num:                # regular division test
              num, prime_factors = prime_division_test(num, prime, prime_factors)
  return (num, prime_factors)

                
# Replace the square_factor_extraction() function with the following version:

def square_factor_extraction(remainder, prime_factors):
    prime_square_remain = []
    for prime in prime_factors:
        squares = prime_factors[prime] // 2
        leftover = prime_factors[prime] - (squares * 2)
        prime_square_remain.append((prime, squares, leftover))
    outside_value = 1   # Product that comes out of the square root
    leftover_product = 1  # Product from the leftover primes (still under the square root)
    for prime, squares, leftover in prime_square_remain:
        if squares > 0:
            outside_value *= prime ** squares
        if leftover > 0:
            leftover_product *= prime ** leftover
    # Multiply in the remaining unfactored part
    inside_value = leftover_product * remainder
    return (outside_value, inside_value)

def remove_unused_prime(prime_factors):
    revised_prime = dict()
    for prime, exponent in prime_factors.items():
        if exponent !=0:
            revised_prime.update({prime:exponent})
    if len(revised_prime) == 0:
        return False
    else:
        return revised_prime
    

def simplify_square_root(num, root):
    prime_factors = sieve_of_eratosthenes(root)

    if prime_factors:                                     # dictionary not empty
        num, prime_factors = factorization_controller(num, prime_factors)
        prime_factors = remove_unused_prime(prime_factors)

        if not prime_factors:                             # square‑free already
            return 1, num

        coefficient, radicand = square_factor_extraction(num, prime_factors)
        return coefficient, radicand

    # fallback when root < 2  (prime list empty)
    return 1, num

    
