n, m = map(int, input().split())

for i in range(n, m+1):
    j = 1
    cnt = 0
    while j < i-1:
        j += 1
        if(i % j == 0):
            cnt += 1
    if cnt == 0:
        print(i)
            
