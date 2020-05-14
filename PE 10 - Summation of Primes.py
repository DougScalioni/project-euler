def is_prime_so_far(n, primes_so_far):
    for p in primes_so_far:
        if n % p == 0:
            return False
    return True


def sum_primes_up_to(n):
    primes = [2]
    sum_primes = 2
    i = 2
    while i <= n:
        if is_prime_so_far(i, primes):
            primes.append(i)
            sum_primes += i
            print(i)
        i += 1

    return sum_primes


print(sum_primes_up_to(2000000))
