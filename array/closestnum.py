"""
Given an array of sorted integers. The task is to find the closest value to the given number in array. Array may contain duplicate values.

Note: If the difference is same for two values print the value which is greater than the given number.
"""


def closestNum(k, a):

    if k >= a[-1]:
        return a[-1]
    if k <= a[0]:
        return a[0]

    else:
        middle = len(a) // 2
        if k == a[middle]:
            return a[middle]
        if k > a[middle]:
            if k < a[middle + 1]:
                if abs(a[middle] - k) == abs(a[middle + 1] - k):
                    return a[middle + 1]
                if abs(a[middle] - k) < abs(a[middle + 1] - k):
                    return a[middle]
                else:
                    return a[middle + 1]
            return closestNum(k, a[middle:])
        else:
            if k > a[middle - 1]:
                if abs(a[middle] - k) == abs(a[middle - 1] - k):
                    return a[middle]
                if abs(a[middle] - k) > abs(a[middle - 1] - k):
                    return a[middle - 1]
                else:
                    return a[middle]
            return closestNum(k, a[: middle])


for i in range(int(input())):
    n, k = map(int, input().rstrip(" ").split())
    array = list(map(int, input().rstrip(" ").split()))
    print(closestNum(k, array))
