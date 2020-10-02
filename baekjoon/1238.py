"""
    gold3 : 파티
    URL = https://www.acmicpc.net/problem/1238
    dijkstra
"""

import sys
import heapq
N = 0
INF = sys.maxsize

def dijkstra(road, s):
    global N, INF

    visited = [False for _ in range(N+1)] 
    min_dist = [INF for _ in range(N+1)] 
    prev_node = [0 for _ in range(N+1)] 
    min_dist[s] = 0
    pq = []
    heapq.heappush(pq, [0, s])

    while pq:
        dist, now = heapq.heappop(pq)
        
        if visited[now] == True:
            continue
        visited[now] = True

        for adj_node, adj_dist in road[now].items():
            if min_dist[adj_node] > dist + adj_dist:
                min_dist[adj_node] = dist + adj_dist
                prev_node[adj_node] = now
                heapq.heappush(pq, [min_dist[adj_node], adj_node])
    
    return min_dist

def main():
    global N, INF

    N, M, X = map(int, sys.stdin.readline().strip().split())

    road = [ {} for _ in range(N+1)]
    rev_road = [ {} for _ in range(N+1)]
    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().strip().split())

        road[s][e] = t
        rev_road[e][s] = t
    
    result = [[] for _ in range(N+1)] 
    '''  solve1) 모든 dijkstra 계산
    answer = 0
    for i in range(1, N+1):
        result[i] = dijkstra(road, i)
    
    for i in range(1, N+1):
        if result[i][X] + result[X][i] > answer:
            answer = result[i][X] + result[X][i]
    print(answer)
    '''
    # solve2) 단방향 방향의 도로를 역으로 하는 road를 만들어서 All_to_X 계산 가능한 방법
    X_to_All = dijkstra(road, X)
    All_to_X = dijkstra(rev_road, X)
    answer = [X_to_All[i] + All_to_X[i] for i in range(1, N+1)]
    print(max(answer))


if __name__=="__main__":
    main()