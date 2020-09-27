"""
    silver1 : 트리
    URL = https://www.acmicpc.net/problem/1068
"""

import sys

def main():
    N = int(sys.stdin.readline().strip())

    tree = [[] for _ in range(N)]
    node_list = list(map(int, sys.stdin.readline().strip().split()))
    root = 0

    for i in range(N):
        if node_list[i] != -1:
            tree[node_list[i]].append(i)
        else:
            root = i
    
    M = int(sys.stdin.readline().strip())

    q = []
    q.append(root)
    answer = 0

    while q:
        tmp = q.pop(0)
        for i in range(len(tree[tmp])):
            if tree[tmp][i] == M:
                del tree[tmp][i]
                break
        if not tree[tmp] and root != M:
            answer += 1

        for i in tree[tmp]:
            if i != M:
                q.append(i)

    print(answer)

if __name__ == "__main__":
    main()