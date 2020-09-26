"""
    silver2 : 트리의 부모 찾기
    URL = https://www.acmicpc.net/problem/11725
"""

import sys

def main():
    N = int(sys.stdin.readline().strip())

    edge = [[] for _ in range(N+1)]
    for _ in range(N-1):
        n1, n2 = map(int, sys.stdin.readline().strip().split())
        edge[n1].append(n2)
        edge[n2].append(n1)
    
    visited = [False for _ in range(N+1)]
    answer = [0 for _ in range(N+1)]
    q = []
    q.append(1)
    while q:
        tmp = q.pop(0)
        visited[tmp] = True

        for i in edge[tmp]:
            if visited[i] == False:
                answer[i] = tmp
                q.append(i)
    
    for i in range(2, N+1):
        print(answer[i])


if __name__ == "__main__":
    main()    