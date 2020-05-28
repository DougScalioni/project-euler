target_sum = 1000


def pythagorean_sum(x, y):
    return x + y + (x ** 2 + y ** 2) ** 0.5


a = 1000
b = 1
ps = pythagorean_sum(a, b)
while ps != 1000:
    print("a:", a, "b:", b, "sum:", ps)
    if ps > 1000 and a > 1:
        a -= 1
    else:
        b += 1
    ps = pythagorean_sum(a, b)

c = (a ** 2 + b ** 2) ** 0.5
print(a*b*c)
