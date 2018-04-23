'''
Given an increasing sequence a[], we need to find the K-th missing
contiguous element in the increasing sequence which is not present in the
sequence. If no k-th missing element is there output -1.
'''


def kthMissingElement(array, k):
    count = 0
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] > 1:
            count += array[i + 1] - array[i] - 1
            if count >= k:
                return array[i + 1] - ((count - k) + 1)
    return -1


if __name__ == "__main__":
    t = int(input())  # test cases

    for i in range(t):
        nk = input().rstrip(" ").split()  # length of array and missingelement's number
        n = int(nk[0])
        k = int(nk[1])
        array = list(map(int, input().rstrip(" ").split()))
        print(kthMissingElement(array, k))
