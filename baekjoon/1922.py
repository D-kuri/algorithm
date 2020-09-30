"""
    gold4 : 네트워크 연결
    URL = https://www.acmicpc.net/problem/1922
    Minimum Spanning Tree / 크루스칼 알고리즘
"""

import sys
root = []
''' union-find시 parent를 바로 위의 값으로 하는경우 
def find(x):
    global root

    if root[x] == x:
        return x
    else:
        return find(root[x])

def union(u, v):
    u_ = min(u, v)
    v_ = max(u, v)
'''

#union-find시 parent를 root로 하는경우
def find(x):
    global root

    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(u, v):
    global root

    u_ = find(min(u, v))
    v_ = find(max(u, v))

    root[v_] = u_

def main():
    global root

    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    root = [i for i in range(N)]
    edge = []
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())

        if a != b:
            a, b = a-1, b-1
            edge.append([a,b,c])

    edge.sort(key=lambda x:x[2])
    cnt = 0
    cost = 0
    for i in edge:
        if find(i[0]) != find(i[1]):
            union(i[0], i[1])
            cost += i[2]
            cnt += 1
        if cnt == N-1:
            break

    print(cost)



if __name__ == "__main__":
    main()