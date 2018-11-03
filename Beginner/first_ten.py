# With a given number n, write a program to generate a dictionary that
# contains (i, i*i) such that i is an number between 1 and n (both included). and
# then the program should print the dictionary.

def dict_(n):
    d = {}
    for i in range(n+1):
        d[i] = i*i
    return d


# 2. Write a program which accepts a sequence of comma-separated
# numbers from console/user and generates a list and a tuple which contains every
# number.

def csn():
    values = input('Enter comma-separated numbers : ')
    values_list = values.split(',')
    values_tuple = tuple(values_list)
    print(values_list)
    print(values_tuple)

print('\n2 :\n')
csn()

# 3. Write a program which will find all the numbers which are divisible by
# 7 but are not a multiple of 5, between 1000 and 1500 (both included). The
# numbers obtained should be printed in a comma-separated sequence on a single
# line.

def sevenNotFive():
    l = []
    for i in range(1000, 1501):
        if i % 7 == 0 and i % 5 != 0:
            l.append(str(i))
    l = ','.join(l)
    print(l)

print('\n 3 :\n')
sevenNotFive()

# 4. Define a function which can compute the sum of two numbers.

def sum(a,b):
    return a+b

print('\n 4 :\n')
print("The sum of 3 and 4 :", sum(3,4))

# 5. Define a function that can receive two integral numbers in string form
# and compute their sum and then print it in console.

def sumPrint(a, b):
    print(f'{int(a)+int(b)}')

print('\n 5 :\n')
print(f"The sum of 3 and 4 :", end=' ')
sumPrint('3','4')

# 6. Write a program which can compute the given factorial of a number.

def factorial(n):
    '''return factorial of n'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 7. Use list comprehension to square each odd number in a list. The list is
# input by a sequence of comma-separated numbers

def sqList():
    '''square each odd number in a list'''
    l = input('Enter comma-separated numbers... :')
    l = l.split(',')
    l = [int(i)**2 for i in l if int(i) % 2 == 1]
    return l

print(sqList())

# 8. Write a program to roll a dice and get a random output (1-6).

import random

def dice():
    return random.randint(1,6)

# 9. Define a function which can generate a dictionary where the keys are
# numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the values only.

def valOnly():
    d = {}
    for i in range(21):
        d[i] = i ** 2
    print(d.values())

valOnly()

# 10. Define a class which has at least two methods: getstring: to get a string
# from user. printstring: to print the string in upper case. Include a test function to test the class methods.

class IOString():
    def __init__(self):
        self.str = ''
    
    def getstring(self):
        self.str = input('Input string ...')
    
    def printstring(self):
        print(self.str.upper())

strObj = IOString()
strObj.getstring()
strObj.printstring()


def test_1():
    assert dict_(1) == {1:1}