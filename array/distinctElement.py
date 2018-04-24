def distinctElem(n):
    distinct_dict = {}
    for i in range(n):
        op, num = input().rstrip(" ").split()
        num = int(num)
        if op == "A":
            if num in distinct_dict:
                distinct_dict[num] += 1
            else:
                distinct_dict[num] = 1
        if op == "R":
            if num in distinct_dict and distinct_dict[num] > 0:
                distinct_dict[num] -= 1
                if distinct_dict[num] == 0:
                    del(distinct_dict[num])
        print(len(distinct_dict))


for i in range(int(input())):
    n = int(input())
    distinctElem(n)
