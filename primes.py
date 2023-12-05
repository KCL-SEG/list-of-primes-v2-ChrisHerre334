"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    # Exclude invalid values
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")
    
    list = []
    current_number = 2

    while len(list) < number_of_primes:
        is_prime = True

        # Check if current_number is divisible by any known prime
        for prime in list:
            if prime * prime > current_number:
                break
            if current_number % prime == 0:
                is_prime = False
                break

        # If current_number is prime, add it to the list
        if is_prime:
            list.append(current_number)

        # Move to the next number
        current_number += 1

    return list
