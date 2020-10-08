"""
    gold2 : 줄 세우기
    URL = https://www.acmicpc.net/problem/2252
    위상정렬(순서가 정해져 있는 작업)
"""

import sys
from collections import deque

def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    sequnce = [[] for _ in range(N+1)]
    edge = [[] for _ in range(N+1)]
    edge_num = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())

        sequnce[a].append(b)
        edge[b].append(a)
    
    for i in range(1, N+1):
        edge_num[i] = len(edge[i])

    q = deque()
    for i in range(1, N+1):
        if not edge[i]:
            q.append(i)
    
    answer = []
    while q:
        tmp = q.popleft()
        answer.append(str(tmp))

        for i in sequnce[tmp]:
            edge_num[i] -= 1
            if edge_num[i] == 0:
                q.append(i)
    
    print(' '.join(answer))
    #print(answer)


if __name__=="__main__":
    main()