"""
    level4 : 게임 맵 최단거리
    URL = https://programmers.co.kr/learn/courses/30/lessons/1844
    bfs 미로 탐색
"""


""" 백준 2178 문제로 테스트 케이스 수행해본 결과
N, M = map(int, input().split())
maps = [ [0 for col in range(M)] for row in range(N)]

for i in range(N):
    a = input()
    for j in range(len(a)):
        maps[i][j] = int(a[j])

queue = [[0,0]]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0] #left, up, right, down
answer = 0
visited = [ [0 for col in range(M)] for row in range(N)]

while(1):
    if not queue:
        break
    out = queue.pop(0)
    x, y = out[0], out[1]

    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]

        if 0 <= next_x < N  and 0 <= next_y < M:
            if visited[next_x][next_y] == 0 and maps[next_x][next_y] == 1:
                queue.append([next_x, next_y])
                visited[next_x][next_y] = visited[x][y] + 1
for i in visited:
    print(i)
if visited[N-1][M-1] == 0:
    answer = -1
else:
    answer = visited[N-1][M-1]+1 """

def solution(maps):

    queue = [[0,0]]
    dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0] #left, up, right, down
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visited = [ [0 for col in range(M)] for row in range(N)]

    while(1):
        if not queue:
            break
        out = queue.pop(0)
        x, y = out[0], out[1]

        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]

            if 0 <= next_x < N  and 0 <= next_y < M:
                if visited[next_x][next_y] == 0 and maps[next_x][next_y] == 1:
                    queue.append([next_x, next_y])
                    visited[next_x][next_y] = visited[x][y] + 1

    if visited[N-1][N-1] == 0:
        answer = -1
    else:
        answer = visited[N-1][N-1]+1
    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
b = [[1,0,1,1,1,1], [1,0,1,0,1,0], [1,0,1,0,1,1], [1,1,1,0,1,1]]
solution(b)