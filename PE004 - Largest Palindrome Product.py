def backwards(string):
    stack = [char for char in string]
    reverse = ''
    for i in range(len(stack)):
        reverse += stack.pop()
    return reverse


def is_palindrome(n):
    return str(n) == backwards(str(n))


# a, b = 999, 999
candidates = []
for a in range(100, 1000):
    b = 999
    while b >= 100:
        p = a * b
        if is_palindrome(p):
            candidates.append(p)
            break
        else:
            b -= 1

print(max(candidates))
