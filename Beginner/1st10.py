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