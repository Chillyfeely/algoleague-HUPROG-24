# Define a function to generate a list of prime numbers up to n using the Sieve of Eratosthenes algorithm.
def sieve(n):
    # Initialize a list of boolean values representing the numbers from 0 to n (inclusive).
    primes = [True] * (n + 1)
    # Set the values for 0 and 1 to False as they are not prime.
    primes[0] = primes[1] = False
    # Iterate over the numbers from 2 to the square root of n (rounded up).
    for i in range(2, int(n**0.5) + 1):
        # If the current number is still marked as prime,
        if primes[i]:
            # Mark its multiples as not prime.
            for j in range(i * i, n + 1, i):
                primes[j] = False
    # Return the list of boolean values, where True indicates that the corresponding number is prime.
    return primes


# Define a function to count the number of prime pairs for each secret key that add up to the key value.
def secret_keys(N, A):
    # Find the maximum key value.
    max_key = max(A)
    # Generate a list of prime numbers up to the maximum key value.
    prime_flags = sieve(max_key)
    # Generate a list of prime numbers from the prime flags.
    prime_list = [i for i, is_prime in enumerate(prime_flags) if is_prime]

    # Iterate over the secret keys.
    for key in A:
        # Initialize the count of prime pairs.
        count = 0
        # Iterate over the prime numbers.
        for prime in prime_list:
            # If the current prime number is greater than half of the key value, break the loop.
            if prime > key // 2:
                break
            # If the difference between the key value and the current prime number is also a prime number,
            if prime_flags[key - prime]:
                # Increment the count of prime pairs.
                count += 1
        # Print the count of prime pairs for the current key.
        print(count)


# Read the number of secret keys from the input.
N = int(input())
# Read the secret keys from the input.
A = list(map(int, input().split()))
# Count the number of prime pairs for each secret key that add up to the key value.
secret_keys(N, A)
