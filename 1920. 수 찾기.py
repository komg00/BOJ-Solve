def lin_search(start, end, array, num):
    mid = (start + end) // 2
    if array[mid] == num:
        return 1
    elif start >= end:
        return 0
    elif num > array[mid]:
        return lin_search(mid+1, end, array, num)
    elif num < array[mid]:
        return lin_search(start, mid-1, array, num)   

n = int(input())
ary = input().split()
m = int(input())
ary2 = input().split()
ary.sort()
for i in range(m):
    print(lin_search(0, n-1, ary, ary2[i]))
