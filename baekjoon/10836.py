"""
    gold4 : 여왕벌
    URL = https://www.acmicpc.net/problem/10836
    구현 / 시뮬레이션
"""
import sys

M, N = map(int, sys.stdin.readline().strip().split())

matrix = [ [1 for col in range(M)] for row in range(M)]
grow = [ 0 for _ in range(2*M-1)]
for i in range(N):
    grow_in = list(map(int, sys.stdin.readline().strip().split()))
    
    for j in range(grow_in[0], grow_in[0] + grow_in[1]):
        grow[j] += 1
    for j in range(grow_in[0] + grow_in[1], 2*M-1):
        grow[j] += 2

now = [M, 0]
dir_xy = [[-1,0], [0,1]]
dir_now = 0

for j in grow:
    now = [now[0]+dir_xy[dir_now][0], now[1]+dir_xy[dir_now][1]]
    matrix[now[0]][now[1]] += j

    if now[0] == 0:
        dir_now = 1
    
for i in range(1, M):
    for j in range(1, M):
        max_ = matrix[i-1][j-1] if matrix[i-1][j-1] >= matrix[i][j-1] else matrix[i][j-1]
        max_ = max_ if max_ >= matrix[i-1][j] else matrix[i-1][j]

        matrix[i][j] = max_

for i in matrix:
    i = list(map(str, i))
    print(' '.join(i))


