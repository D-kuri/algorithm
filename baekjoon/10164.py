"""
    silver1 : 격자상의 경로
    URL = https://www.acmicpc.net/problem/10164
    수학문제
"""

import math

N, M, K = map(int, input().split())

x, y = 0, 0

''' def factorial(n):
    if(n==1):
        return 1
    else:
        return n * factorial(n-1) '''

num = 1
if(K != 0):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if(num == K):
                x = j-1
                y = i-1
            num += 1
    distance_1 = math.factorial(x+y) / (math.factorial(x) * math.factorial(y))
    distance_2 = math.factorial(M+N-(x+y+2)) / (math.factorial(M-(x+1)) * math.factorial(N-(y+1)))
else:
    distance_1 = 1
    distance_2 = math.factorial(M+N-2) / (math.factorial(M-1) * math.factorial(N-1))

print(int(distance_1 * distance_2))