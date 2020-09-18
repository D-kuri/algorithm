"""
    gold3 : LCA
    URL = https://www.acmicpc.net/problem/11437
    LCA 알고리즘(최소 공통 조상)
"""

import sys
from math import log2

visited = []
dep = []
ancestor = []
answer = []
log = 0

def dfs(now, parent, depth, edge):
    global visited, dep, ancestor, log
    visited[now] = True
    dep[now] = depth
    ancestor[now][0] = parent

    for i in edge[now]:
        if visited[i] == False:
            dfs(i, now, depth+1, edge)



def main():
    global visited, answer, dep, ancestor, log

    N = int(sys.stdin.readline().strip())
    log = int(log2(N)+1)
    edge = [[] for _ in range(N+1)]
    ancestor = [[0 for _ in range(log)] for i in range(N+1)]

    for _ in range(N-1):
        n1, n2 = map(int, sys.stdin.readline().strip().split())
        edge[n1].append(n2)
        edge[n2].append(n1)

    visited = [False for _ in range(N+1)]
    dep = [0 for _ in range(N+1)]

    #dfs(1, 0, 0, edge)
    q = []
    q.append(1)
    while q:
        tmp = q.pop(0)
        visited[tmp] = True
        for i in edge[tmp]:
            if visited[i] == False:
                q.append(i)
                ancestor[i][0] = tmp
                dep[i] = dep[tmp] + 1
    for j in range(1, log):
        for i in range(1, N+1):
            ancestor[i][j] = ancestor[ancestor[i][j-1]][j-1]


    """ print("-----------------")
    print(dep)
    for i in ancestor:
        print(i)
    print("----------------") """

    M = int(sys.stdin.readline().strip())

    for _ in range(M):
        n1, n2 = map(int, sys.stdin.readline().strip().split())
        
        if dep[n1] != dep[n2]:
            if dep[n1] > dep[n2]:
                n1, n2 = n2, n1
            
            for i in range(log-1, -1, -1):
                if ancestor[n2][i] != 0 and dep[n1] <= dep[ancestor[n2][i]]:
                    n2 = ancestor[n2][i]
        
        if n1 == n2:
            answer.append(n1)
            continue
        else:
            for i in range(log-1, -1, -1):
                if ancestor[n1][i] != ancestor[n2][i]:
                    n1 = ancestor[n1][i]
                    n2 = ancestor[n2][i]
        
        answer.append(ancestor[n1][0])

    for i in answer:
        print(i)
    
if __name__ == '__main__':
    main()