N = 600851475143


def is_prime_so_far(n, primes_so_far):
    for p in primes_so_far:
        if n % p == 0:
            return False
    return True


def primes_up_to(n):
    primes = [2]
    i = 2
    while i < n:
        while not is_prime_so_far(i, primes):
            i += 1
        primes.append(i)
    return primes


def prime_factors(n):
    factors = []
    sqrt = int(n ** 0.5) + 1
    primes = primes_up_to(sqrt)
    for p in primes:
        if n % p == 0:
            factors.append(p)
            n /= p
    return factors


print(prime_factors(N))

