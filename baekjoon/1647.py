
"""
    gold4 : 도시 분할 계획
    URL = https://www.acmicpc.net/problem/1647
    Minimum Spanning Tree / Prim 알고리즘
"""

import sys
N = 0
INF = sys.maxsize
def prim(graph):
    global N, INF
    
    key = [INF] * N
    parent = [None] * N
    visited = [False] * N
    key[0] = 0
    parent[0] = -1

    for _ in range(N):
        visit_vertex = -1

        min_ = INF
        for i in range(N):
            if not visited[i] and key[i] < min_:
                min_ = key[i]
                visit_vertex = i
        
        visited[visit_vertex] = True
        for j in range(N):
            if not visited[j] and graph[visit_vertex][j] > 0 and graph[visit_vertex][j] < key[j]:
                key[j] = graph[visit_vertex][j]
                parent[j] = visit_vertex
    
    print(sum(key)-max(key))
    ''' for i in range(N):
        answer += graph[i][parent[i]] '''
    


def main():
    global N

    N, M = map(int, sys.stdin.readline().strip().split())
    graph = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        a,b,c = map(int, sys.stdin.readline().strip().split())
        a,b = a-1,b-1

        graph[a][b] = c
        graph[b][a] = c
    
    prim(graph)

if __name__=="__main__":
    main()