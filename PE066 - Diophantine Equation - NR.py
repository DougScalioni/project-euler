def diophantine_quadratic(d, n):
    x = 1
    y = 1
    while x ** 2 - d * (y ** 2) != 1:
        if x ** 2 - d * (y ** 2) > d:
            y += 1
        else:
            x += 1
            #print(x, y)
    return x, y


def is_square(x):
    sqrt = x ** 0.5
    remainder = sqrt - int(sqrt)
    return remainder == 0

solutions_x = []
for i in range(1000):
    if is_square(i):
        print("square")
    else:
        print(i+1)
        print(diophantine_quadratic(i+1, 1))
