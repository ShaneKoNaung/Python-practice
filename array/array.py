# practice using array in python
def array_test():
    a = [1, 2, 3, 4]

    print("Original array: ", a)

    print("adding 5 at the end of the array:", end=" ")
    a.append(5)
    print(a)

    print("Index of 5:",  a.index(5))

    print("Removing the first occurence of 3:", end=" ")
    a.remove(3)
    print(a)

    print("Reversing the array:", end=" ")
    a.reverse()
    print(a)

    print("Sorting the array:", end=" ")
    a.sort()
    print(a)

    print("removing the last element of the array:", end=" ")
    a.pop()
    print(a)

    print("deleting element in index 1 from the array", end=" ")
    del a[1]
    print(a)

    print("The length of the array: ", len(a))

    print("Inserting the value of 10 at the index 2:", end=" ")
    a.insert(2, 10)
    print(a)
    

def main():
    array_test()


if __name__ == "__main__":
    main()
