# 22. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
# print this list after removing all duplicate values with original order reserved.

l = [12,24,35,24,88,120,155,88,120,155]

def rmdup(l):
    ''' remove all duplicates in l'''
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list

new = rmdup(l)
print(new)