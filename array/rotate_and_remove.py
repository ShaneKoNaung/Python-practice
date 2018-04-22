# rotate and delete an array
# rotate the array in clockwise direction n times and remove the nth element
# each time
# if there is no nth element, remove the first element


# rotate the array in clockwise direction
def rotateArray(a):
    lastElement = a.pop()
    a.insert(0, lastElement)
    return a


# rotate the array n times and remove the nth element
def rotateNTimesAndRemove(n, a):
    if n == 1:
        print(a[0])
    for i in range(n):
        a = rotateArray(a)
        try:
            del a[-1 - i]  # delete the nth element
        except IndexError:
            del a[0]      # if there is no nth element remove the first element
        if len(a) == 1:
            print(a[0])


if __name__ == "__main__":
    t = int(input())  # number of test cases
    for i in range(t):
        n = int(input())  # length of array
        array = list(input().rstrip(" ").split())
        array = list(map(int, array))
        rotateNTimesAndRemove(n, array)
