def is_prime_so_far(n, primes_so_far):
    for p in primes_so_far:
        if n % p == 0:
            return False
    return True


def n_first_primes(n):
    primes = [2]
    i = 2
    for m in range(1,n):
        while not is_prime_so_far(i, primes):
            i += 1
        primes.append(i)
    return primes


print(n_first_primes(10001)[-1])
