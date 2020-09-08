"""
    gold1 : 제곱ㄴㄴ수
    URL = https://www.acmicpc.net/problem/1016
"""
a = input().split()
min = int(a[0])
max = int(a[1])

check = [True for i in range(max-min+1)]

for i in range(2, max):
    square = i*i
    if(square > max):
        break
    
    start = min
    if(min % square == 0):
        pass
    else:
        start = min + (square - (min%square))

    for j in range(start, max+1, square):
        check[j-min] = False

cnt = 0
for i in range(len(check)):
    if(check[i] == True):
        cnt += 1

print(cnt)