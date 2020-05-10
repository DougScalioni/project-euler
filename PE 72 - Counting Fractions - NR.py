def HCF(n, d):  # numerator, denominator. Here it's assumed that n is always less than or equal to d
    r = d % n
    if r == 0:
        return n
    else:
        return HCF(r, n)

print(HCF(4,9))
