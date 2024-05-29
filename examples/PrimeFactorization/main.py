import numpy as np
import sys
def prime_factors(n):
    factors = []
    # Divide by 2 until n becomes odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors using NumPy's arange for efficiency
    for i in np.arange(3, int(np.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

def main(args):
    if len(args) != 2:
        print("Usage: python main.py <number>")
        return
    try:
        n = int(args[1])
        if n < 2:
            print("Number must be greater than 1.")
            return
        factors = prime_factors(n)
        print(f"Prime factors of {n} are: {factors}")
    except ValueError:
        print("Invalid number format.")
    return

if __name__ == "__main__":

    main(sys.argv)
