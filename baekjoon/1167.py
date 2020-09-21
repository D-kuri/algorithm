"""
    gold3 : 트리의 지름
    URL = https://www.acmicpc.net/problem/1167
    dfs
"""

import sys
sys.setrecursionlimit(10**6)
visited = []
answer = 0
tmp = [0,0]

def dfs(n1, edge, distance):
    global visited, answer, tmp
    if tmp[0] < distance:
        tmp[0] = distance
        tmp[1] = n1

    visited[n1] = True
    for i in edge[n1]:
        if visited[i[0]] == False:
            dfs(i[0],  edge, distance+i[1])


def main():
    global visited, answer, tmp

    N = int(sys.stdin.readline().strip())
    edge = [[] for _ in range(N+1)]

    for _ in range(N):
        edge_list = list(map(int, sys.stdin.readline().strip().split()))

        for i in range(1, len(edge_list), 2):
            if edge_list[i] == -1:
                break
            edge[edge_list[0]].append([edge_list[i], edge_list[i+1]])

    distance = 0
    visited = [False for _ in range(N+1)]
    dfs(1, edge, distance)

    distance = 0
    visited = [False for _ in range(N+1)]
    dfs(tmp[1], edge, distance)
    print(tmp[0])
    ''' for i in range(1, N+1):
        visited = [False for _ in range(N+1)]
        distance = 0
        dfs(i, edge, distance)
        if answer < tmp:
            answer = tmp
     '''

if __name__ == '__main__':
    main()