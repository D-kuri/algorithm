"""
    gold5 : 최단경로
    URL = https://www.acmicpc.net/problem/1753
    dijkstra
"""

import sys
import heapq
V = 0
INF = sys.maxsize

def dijkstra(edge, K):
    global V, INF

    prev_node = [0 for _ in range(V+1)] #k에서 시작해서 연결된 노드 순서중 현재 노드 전 방문 노드
    min_dist = [INF for _ in range(V+1)] #k에서의 최소 거리들을 나타내는 배열
    visited = [False for _ in range(V+1)] #방문여부
    min_dist[K] = 0
    pq = []
    heapq.heappush(pq, [0, K])

    while pq:
        dist, now = heapq.heappop(pq)
        if visited[now] == True:
            continue
        
        visited[now] = True

        for adj_node, adj_dist in edge[now].items():
            if min_dist[adj_node] > dist + adj_dist:
                min_dist[adj_node] = dist + adj_dist
                heapq.heappush(pq, [min_dist[adj_node], adj_node])

                prev_node[adj_node] = now
    
    return min_dist


def main():
    global V, INF

    V, E = map(int, sys.stdin.readline().strip().split())
    K = int(sys.stdin.readline().strip())

    edge = [ {} for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().strip().split())

        if v in edge[u]:
            edge[u][v] = min(edge[u][v], w)
        else:
            edge[u][v] = w
    
    K_to_dist = dijkstra(edge, K)

    for i in range(1, V+1):
        if K_to_dist[i] == INF:
            print("INF")
        else:
            print(K_to_dist[i])


if __name__ == "__main__":
    main()
