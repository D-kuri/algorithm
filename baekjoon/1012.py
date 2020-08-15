"""
    silver2 : 유기농배추
    URL = https://www.acmicpc.net/problem/1012
    DFS 문제
"""

T = int(input())

tmp = [[-1,0], [0,-1], [1,0], [0,1]]
result = []

def check_set(x,y, field):
    if(field[x][y] == 0):
        return
    else:    
        field[x][y] = 0
    
    check = []
    for i in tmp:
        check.append([i[0]+x,i[1]+y])

    for i in check:
        if(i[0] < 0 or i[0] >= len(field) or i[1] < 0 or i[1] >= len(field[0])):
            pass
        else:
            check_set(i[0], i[1], field)


for i in range(0, T):
    M, N, K = map(int, input().split())
    result_tmp = 0
    #field = [[0] * M] * N
    field = [[0 for col in range(M)] for row in range(N)]
    for j in range(0, K):
        x,y = map(int, input().split())
        field[y][x] = 1
    
    for a in range(0, N):
        for b in range(0, M):
            if(field[a][b] == 0):
                pass
            else:
                check_set(a, b, field)
                result_tmp += 1
    
    result.append(result_tmp)

for i in result:
    print(i)