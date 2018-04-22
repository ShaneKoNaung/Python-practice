def factors(a):
    total = 1
    for i in a:
        total *= i
    return total


print(factors([24, 63, 10]))
