# 11. Define a class, which have a class parameter and have a same instance parameter.

class Dog:
    # class parameter   
    name = 'Dog'

    # instance parameter
    def __init__(self, name=None):
        self.name = name

print('\n 11 : \n')    
A = Dog()
A.name = 'Jackie'
print(f'{Dog.name} is {A.name}')
print('---------------------------------------------')

# 12. Write a program that accepts a sentence and calculates the number of upper and lower case letters.
def upOrLow():
    s = input('Enter :')
    up, low = 0, 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    return up, low

up, low = upOrLow()
print('\n 12 :\n')
print(f'Upper : {up} \nLower : {low} \n')
print('---------------------------------------------')

# 13. Write a program to display the fibonacci series up to the nth term

def fab(n):
    n1 = 0
    n2 = 1
    i = 0
    while i < n:
        i += 1
        n1, n2 = n2, n1 + n2
    return n1

print('\n 13 : \n')
print(f'fibonacci of 10 : {fab(10)}')
print('---------------------------------------------')

# 14. Define a class named American and its subclass NewYorker.
class American(object):
    pass

class NewYorker(American):
    pass

# 15. Define a class named Circle which can be constructed by a radius. The
# Circle class has a method which can compute the area.

class Circle(object):
    def __init__(self, radius):
        self.r = radius
    
    def area(self):
        return 3.14 * (self.r **2)

print('\n 15 :\n')
a = Circle(10)
print(f'Area of circle with radius {a.r} is {a.area()}')
print('------------------------------------')


# 16. Write a program using generator to print the even numbers between 0 and n
# in comma separated form while n is input by console.

def EvenGenerator(n):
    val = 0
    while val < n:
        yield val
        val += 2

print('\n 16 \n')
n = int(input('Enter an integer :'))
values = []
for i in EvenGenerator(n): 
    values.append(str(i))
print(','.join(values))
print('----------------------------------------')

# 17. Write statements using assert expression to verify that every number in the list
# [2,4,6,8] is even.

l = [2, 4, 6, 8]
for i in l:
    assert i % 2 == 0

# 18. Write a program to compress and decompress the string "Hello
# world! Python is great!".

import zlib

print('\n 18 : \n')
s = 'Hello world! Python is great!'
compress = zlib.compress(s.encode('utf-8'))
print(compress)
print(zlib.decompress(compress))
print('----------------------------------------')

# 19. Define three individual functions to implement the filter, map and reduce
# functions. Experiment on them as you like.

import functools

print('\n 19 : \n')
def isOdd(n) : 
    return n % 2 == 1
print(list(filter(isOdd, range(20))))

def square(n) : return n * n
print(list(map(square, range(10))))

def add(a, b) : return a + b
print(functools.reduce(add, range(3)))
print('---------------------------------------------------')

# 20. Create a list of integers. Using filter and lambda functions find the integers
# that are multiples of 3. Using map and lambda functions multiply all integers of
# the list by 2 and add 15. Use the reduce function from functools module to simply add all integers.

a = range(20)
print('\n 20 :\n')
print(f'integers that are multiples of 3 : {list(filter(lambda x: x % 3 == 0, a))}')
print(f'multiply all integers of the list by 2 and add 15 : {list(map(lambda x: (x * 2) + 15, a))}')
print(f'add all integers : {functools.reduce(lambda x, y: x + y, a)}')
print('------------------------------------------------------')
