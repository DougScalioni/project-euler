def multiple_3(x):
    digits = list(str(x))
    sum_digits = 0
    for n in digits:
        sum_digits += int(n)
    if sum_digits >= 10:
        return multiple_3(sum_digits)
    else:
        return sum_digits % 3 == 0


def multiple_5(x):
    digits = list(str(x))
    return digits[-1] == '0' or digits[-1] == '5'


multiples = []
for i in range(1000):
    if multiple_3(i) or multiple_5(i):
        multiples.append(i)
sum_total = sum(multiples)
print(sum_total)
