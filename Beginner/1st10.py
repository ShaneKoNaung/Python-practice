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

# 2. Write a program which accepts a sequence of comma-separated
# numbers from console/user and generates a list and a tuple which contains every
# number.

def csn():
    values = input('Enter comma-separated numbers : ')
    values_list = values.split(',')
    values_tuple = tuple(values_list)
    print(values_list)
    print(values_tuple)

print('2 :\n')
csn()
