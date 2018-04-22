# using temp array
def rotate_temp(a, n):
    temp = a[:n]
    a = a[n:] + temp
    return a


# rotating one by one
def rotate_onebyone(a, n):
    for i in range(n):
        temp = a[0]
        a = a[1:]
        a.append(temp)
    return a


def main(n, a):
    print(rotate_temp(a, n))
    print(rotate_onebyone(a, n))


if __name__ == "__main__":
    n = int(input())  # number of spaces to shift
    a = input().rstrip(" ").split()  # array to shift
    # making the elements int
    a = list(map(int, a))
    main(n, a)
