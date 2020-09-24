"""
    gold3 : ACM Craft
    URL = https://www.acmicpc.net/problem/1005
    위상정렬(순서가 정해져 있는 작업)
"""

import sys
sys.setrecursionlimit(10**6)

def main():
    T = int(sys.stdin.readline().strip())
    answer = []

    for _ in range(T):
        N, K = map(int, sys.stdin.readline().strip().split())
        time = list(map(int, sys.stdin.readline().strip().split()))
        time.insert(0,0)
        rule = [[] for _ in range(N+1)]
        parent = [[] for _ in range(N+1)]
        total_time = [0 for _ in range(N+1)]
        inDegree = [0 for _ in range(N+1)]

        for _ in range(K):
            building_num, building_time = map(int, sys.stdin.readline().strip().split())
            rule[building_num].append(building_time)
            parent[building_time].append(building_num)
        
        for i in range(N+1):
            inDegree[i] = len(parent[i])
        
        W = int(sys.stdin.readline().strip())

        q = []
        for i in range(1, N+1):
            if not parent[i]:
                q.append(i)
        
        check = 0
        while q:
            next_ = q.pop(0)

            for i in rule[next_]:
                inDegree[i] -= 1
                if not inDegree[i]:
                    q.append(i)

                    max_time = 0
                    for j in parent[i]:
                        if max_time < time[j]:
                            max_time = time[j]
                    time[i] += max_time
                
                    if i == W:
                        check = 1
                        break
            
            if check == 1:
                break
        
        
        answer.append(time[W])
    for i in answer:
        print(i)


if __name__ == "__main__":
    main()

""" 
stack = []
for j in build_rule[W-1]:
    stack.append(j)

print(build_rule)

for i in range(T):
    N, K = map(int, input().split())

build_time = list(map(int,input().split()))

build_rule = [ [] for i in range(K)]
print(build_time)

for j in range(K):
    X, Y = map(int, input().split())
    build_rule[Y-1].append(X-1)

W = int(input())

stack = []
for j in build_rule[W-1]:
    stack.append(j)

print(build_rule) 
"""
