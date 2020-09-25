"""
    gold4 : 작업
    URL = https://www.acmicpc.net/problem/2056
    위상정렬(순서가 정해져 있는 작업)
"""

import sys

def main():
    N = int(sys.stdin.readline().strip())

    child = [[] for _ in range(N+1)]
    parent = [[] for _ in range(N+1)]
    edge_num = [0 for _ in range(N+1)]
    time = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        work = list(map(int, sys.stdin.readline().strip().split()))

        time[i] = work[0]
        parent_num = work[1]
        for j in range(parent_num):
            parent[i].append(work[j+2])
            child[work[j+2]].append(i)
    
    for i in range(1, N+1):
        edge_num[i] = len(parent[i])

    tmp = []
    for i in range(1, N+1):
        if not parent[i]:
            tmp.append(i)
    
    for a in tmp:
        q = []
        q.append(a)
        while q:
            next_ = q.pop(0)

            for i in child[next_]:
                edge_num[i] -= 1

                if edge_num[i] == 0:
                    q.append(i)

                    max_time = 0
                    for j in parent[i]:
                        if max_time < time[j]:
                            max_time = time[j]
                    time[i] += max_time
    
    print(max(time))


if __name__ == "__main__":
    main()