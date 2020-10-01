"""
    gold1 : 전기가 부족해
    URL = https://www.acmicpc.net/problem/10423
    Minimum Spanning Tree / 크루스칼 알고리즘
"""

import sys
root = []
power = []

def find(x):
    global root

    if root[x] == x:
        return x
    else:
        return find(root[x])

def union(u, v):
    global root, power

    u = find(u)
    v = find(v)

    check = 0
    for i in power:
        if i == u:
            check = 1
            root[v] = u
            break
        elif i == v:
            check = 1
            root[u] = v
            break
    
    if check == 0:
        root[u] = v
    

def main():
    global root, power

    N, M, K = map(int, sys.stdin.readline().strip().split())
    power = list(map(int, sys.stdin.readline().strip().split()))
    edge = []
    root = [i for i in range(N)]

    for i in range(len(power)):
        power[i] -= 1


    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().strip().split())
        u, v = u-1, v-1
        edge.append([u, v, w])
    
    edge.sort(key=lambda x:x[2])
    cnt = K-1
    cost = 0

    for i in edge:
        f1 = find(i[0])
        f2 = find(i[1])
        if f1 != f2:
            check = 0
            for j in power:
                if j==f1 or j==f2:
                    check += 1
                if check == 2:
                    break
            
            if check != 2:
                #print(i[0]+1, i[1]+1)
                union(i[0], i[1])
                cnt += 1
                cost += i[2]
        if cnt == N-1:
            break
    print("-----------")
    for i in range(N):
        print(find(i)+1)
    print(cost)


if __name__=="__main__":
    main()