"""
    platinum5 : 정점들의 거리
    URL = https://www.acmicpc.net/problem/1761
    LCA 알고리즘(최소 공통 조상)
"""

import sys
sys.setrecursionlimit(10**6)
visited = []
dep = []
ancestor = []
answer = []

def main():
    global visited, answer, dep, ancestor

    N = int(sys.stdin.readline().strip())
    edge = [[] for _ in range(N+1)]
    ancestor = [[0 for _ in range(16)] for _ in range(N+1)]

    for _ in range(N-1):
        n1, n2, cost = map(int, sys.stdin.readline().strip().split())
        edge[n1].append([n2, cost])
        edge[n2].append([n1, cost])

    visited = [False for _ in range(N+1)]
    dep = [0 for _ in range(N+1)]
    cost = [0 for _ in range(N+1)]
    q = []
    q.append(1)
    while q:
        tmp = q.pop(0)
        visited[tmp] = True

        for i in edge[tmp]:
            if visited[i[0]] == False:
                q.append(i[0])
                ancestor[i[0]][0] = tmp
                dep[i[0]] = dep[tmp] + 1
                cost[i[0]] = cost[tmp] + i[1]
    
    for j in range(1, 16):
        for i in range(1, N+1):
            ancestor[i][j] = ancestor[ancestor[i][j-1]][j-1]
    """ print(cost)
    print("------")
    print(dep)
    for i in ancestor:
        print(i) """
    



    M = int(sys.stdin.readline().strip())

    for _ in range(M):
        n1, n2 = map(int, sys.stdin.readline().strip().split())
        start1, start2 = n1, n2
        
        if dep[n1] != dep[n2]:
            if dep[n1] > dep[n2]:
                n1, n2 = n2, n1
            
            
            for i in range(15, -1, -1):
                if ancestor[n2][i] != 0 and dep[n1] <= dep[ancestor[n2][i]]:
                    n2 = ancestor[n2][i]
        
        if n1 == n2:
            answer.append((cost[start1] - cost[n1]) + (cost[start2] - cost[n1]))
            continue
        else:
            for i in range(15, -1, -1):
                if ancestor[n2][i] != ancestor[n1][i]:
                    n1 = ancestor[n1][i]
                    n2 = ancestor[n2][i]
        
        answer.append((cost[start1] - cost[ancestor[n1][0]]) + (cost[start2] - cost[ancestor[n2][0]]))

    for i in answer:
        print(i)     



    
if __name__ == '__main__':
    main()



""" import sys
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

    N = int(sys.stdin.readline().strip())
    edge = [[] for _ in range(N+1)]

    for _ in range(N-1):
        n1, n2, cost = map(int, sys.stdin.readline().strip().split())
        edge[n1].append([n2, cost])
        edge[n2].append([n1, cost])


    M = int(sys.stdin.readline().strip())
    for _ in range(M):
        visited = [False for _ in range(N+1)]
        n1, n2 = map(int, sys.stdin.readline().strip().split())

        distance = 0
        dfs(n1, n2, edge, distance)
    
    for i in answer:
        print(i)

if __name__ == '__main__':
    main() """