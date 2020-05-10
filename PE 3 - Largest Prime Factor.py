import sympy
N = 600851475143


def diff(list_a, list_b):
    for item in list_b:
        if item in list_a:
            list_a.remove(item)
    return list_a


def primes_up_to(n):
    li = list(range(2, n))
    primes = []
    while len(li) > 0:
        # print(li)
        i = li[0]
        rg = int(n / i)
        subtract = [item * i for item in list(range(1, rg + 1))]
        li = diff(li, subtract)

        primes.append(i)
    return primes


def prime_factors(n):
    factors = []
    sqrt = int(n ** 0.5) + 1
    primes = list(sympy.primerange(2, sqrt))

    for p in primes:
        if n % p == 0:
            factors.append(p)
            n /= p
    return factors

print(prime_factors(N))
