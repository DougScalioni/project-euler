def divisors(n):
    div = set([1])
    i = 2
    while n > 1:
        if n % i == 0:
            n = n / i
            add_div = set([])
            for d in div:
                add_div.add(d * i)
            div = div | add_div
            i = 2
        else:
            i += 1
    return div


def n_divisors(n):
    divs = divisors(n)
    return len(divs)


i = 1
t = 1
divs = n_divisors(t)
while divs <= 500:
    i += 1
    t += i
    divs = n_divisors(t)
print(t)
