"""
    gold4 : 최소 스패닝 트리
    URL = https://www.acmicpc.net/problem/10164
    수학문제
"""

V, E = map(int, input().split())

cycle = []
result = 0

for i in range(V):
    cycle.append(i)


before_sort = []
after_sort = []

for i in range(E):
    v1, v2, C = map(int, input().split())
    before_sort.append([v1,v2,C])

after_sort = sorted(before_sort, key=lambda x:x[2])

def root(x):
    global cycle

    if(cycle[x] == x):
        
        return x
    else:
        cycle[x] = root(cycle[x])
        return cycle[x]

def union(u_, v_):
    u = root(min(u_ ,v_))
    v = root(max(u_, v_))

    cycle[v] = u

count = 0

def check_cycle(u, v, c):
    global V, cycle, result, count

    if(root(u) != root(v)):
        check = union(u, v)
        result += c
        count += 1
    
for i in after_sort:
    check_cycle(i[0]-1, i[1]-1, i[2])

    """ if(cycle.count(0) == V):
        break """
    if(count == V-1):
        break


print(result)


""" 
V, E = map(int, input().split())

cycle = []
result = 0

for i in range(V):
    cycle.append([i])

#graph = [[0 for col in range(V)] for row in range(V)]

before_sort = []
after_sort = []

for i in range(E):
    v1, v2, C = map(int, input().split())
    before_sort.append([v1,v2,C])
    #graph[v1-1][v2-1] = C
    #graph[v2-1][v1-1] = C

after_sort = sorted(before_sort, key=lambda x:x[2])

def check_cycle(u, v, c):
    global cycle, result
    index_u, index_v = -1, -1
    reduce_time = 0
    for i in range(len(cycle)):
        if(reduce_time == 2):
            break
        if(cycle[i].count(u) == 1 and cycle[i].count(v) == 1 ):
            break
        else:
            if(cycle[i].count(u) == 1):
                index_u = i
                reduce_time += 1
            if(cycle[i].count(v) == 1):
                index_v = i
                reduce_time += 1
    

    if(index_u+index_v != -2):
        cycle[index_u].extend(cycle[index_v])
        del cycle[index_v]
        #cycle.remove[cycle[index_v]]
        result += c

for i in after_sort:
    check_cycle(i[0]-1, i[1]-1, i[2])
    if(len(cycle) == 1):
        break

print(result)
 """


""" 
stack = []
check_point = [ 0 for a in range(V) ]
check_point[0] = 1

def dfs(v_start):
    global V, stack, check_point
    check_point[v_start] = 1

    for i in range(v_start+1, V):
        stack.append(i)
        if(graph[v_start][i] == 0):
            pass
        else:
            stack.append(i)
            dfs(i)
 """

