from array import array

print('initializing an array')
a = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print(a)
print()

print("The size of one item in bytes: ", end=" ")
print(a.itemsize)
print()

print("Append a new item at the end of the array")
a.append(1)
print(a)
print()

print("Number of occurences of 1 in the array")
print(a.count(1))
print()

print("Append items form iterable to the end of the array")
a.extend([1, 2, 3])
print(a)
print()

print("Append items form the list")
alist = [4, 2, 52, 44]
a.fromlist(alist)
print(a)
print()

print("The index of the first occurence of 8")
print(a.index(8))
print()

print("Remove the item from the index 10 from the array")
a.pop(10)
print(a)
print()

print("Remove the first occurence of x from the array")
a.remove(8)
print(a)
print()

print("convert the array to the list")
alist = a.tolist()
print(alist)
print()
