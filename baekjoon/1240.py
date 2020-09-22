"""
    gold4 : 노드사이의 거리
    URL = https://www.acmicpc.net/problem/1240
    dfs
"""

import sys
sys.setrecursionlimit(10**6)
visited = []
answer = []

def dfs(n1, n2, edge, distance):
    global visited, answer
    if n1 == n2:
        answer.append(distance)
        return 0

    visited[n1] = True
    for i in edge[n1]:
        if visited[i[0]] == False:
            if dfs(i[0], n2, edge, distance+i[1]) == 0:
                return 0


def main():
    global visited, answer

    N, M = map(int, sys.stdin.readline().strip().split())
    edge = [[] for _ in range(N+1)]

    for _ in range(N-1):
        n1, n2, cost = map(int, sys.stdin.readline().strip().split())
        edge[n1].append([n2, cost])
        edge[n2].append([n1, cost])


    for _ in range(M):
        visited = [False for _ in range(N+1)]
        n1, n2 = map(int, sys.stdin.readline().strip().split())

        distance = 0
        dfs(n1, n2, edge, distance)
    
    for i in answer:
        print(i)

if __name__ == '__main__':
    main()