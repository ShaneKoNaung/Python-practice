# 21. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
# console (n>0). 

n = int(input('Enter an integer ... : '))
res = 0
for i in range(1, n+1):
    res += i/(i + 1)
print(res)
