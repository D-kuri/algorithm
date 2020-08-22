"""
    Level3 : 배달
    URL = https://programmers.co.kr/learn/courses/30/lessons/12978
    Summer/Winter Coding(~2018)
"""

""" N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
 """
N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

count = 0

def dijkstra(visit_node, now_node, shortest_path, path):
    global count
    count += 1

    next_node = [0, 999999]
    for i in range(len(visit_node)):
        if(path[now_node][i] == 0):
            pass
        else:
            shortest_path[i] = shortest_path[i] if shortest_path[i] < shortest_path[now_node] + path[now_node][i] else shortest_path[now_node] + path[now_node][i]

    for i in range(len(visit_node)):
        if(visit_node[i] == True):
            pass
        
        else:
            if(next_node[1] > shortest_path[i]):
                next_node[0] = i
                next_node[1] = shortest_path[i]

    if(count == len(visit_node)):
        pass
    else:
        visit_node[next_node[0]] = True
        dijkstra(visit_node, next_node[0], shortest_path, path)

def solution(N, road, K):
    path = [[0 for col in range(N)] for row in range(N)]

    for i in range(len(road)):
        if(path[road[i][0]-1][road[i][1]-1] == 0):
            path[road[i][0]-1][road[i][1]-1] = road[i][2]
            path[road[i][1]-1][road[i][0]-1] = road[i][2]
        else:
            path[road[i][0]-1][road[i][1]-1] = path[road[i][0]-1][road[i][1]-1] if path[road[i][0]-1][road[i][1]-1] < road[i][2] else road[i][2]
            path[road[i][1]-1][road[i][0]-1] = path[road[i][0]-1][road[i][1]-1] if path[road[i][0]-1][road[i][1]-1] < road[i][2] else road[i][2]

    visit_node = [False] * N
    shortest_path = [99999999] * N
    visit_node[0] = True
    shortest_path[0] = 0
    now_node = 0

    dijkstra(visit_node, now_node, shortest_path, path)
    #print(shortest_path)
    answer = 0
    for i in shortest_path:
        if(i <= K):
            answer += 1

    return answer


solution(N, road, K)