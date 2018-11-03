# With a given number n, write a program to generate a dictionary that
# contains (i, i*i) such that i is an number between 1 and n (both included). and
# then the program should print the dictionary.

def dict_(n):
    d = {}
    for i in range(n+1):
        d[i] = i*i
    print(d)
print('1 :\n')
dict_(10)
