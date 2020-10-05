"""
    gold3 : 소문난칠공주
    URL = https://www.acmicpc.net/problem/1941
    백트래킹
"""

import sys
import copy
from itertools import combinations
dx, dy = [-1,0,1,0], [0,1,0,-1] #up, right, down, left

def bfs(seven, array):
    seven_tmp = copy.deepcopy(seven)
    for i in range(7):
        seven_tmp[i].append(i)
    visited = [False for _ in range(7)]
    q = []
    q.append(seven_tmp[0])
    check_num = 0

    
    while q:
        now_x, now_y, index = q.pop(0)

        if visited[index]:
            continue

        visited[index] = True
        check_num += 1

        if check_num == 7:
            break

        for i in range(4):
            move_x, move_y = now_x + dx[i], now_y + dy[i]
            for x, y, num in seven_tmp:
                if x == move_x and y == move_y:
                    if not visited[num]:
                        q.append(seven_tmp[num])
    
    if check_num == 7:
        return 1
    else:
        return 0

def main():
    array = []
    comb = []
    for i in range(5):
        for j in range(5):
            comb.append([i,j])
        tmp = list(sys.stdin.readline().strip())
        array.append(tmp)
    
    comb = list(combinations(comb, 7))
    answer = 0

    for seven in comb:
        check = 0
        for i in seven:
            if array[i[0]][i[1]] == "Y":
                check += 1
            if check > 3:
                break
        
        if check > 3:
            continue
        
        answer += bfs(seven, array)

    print(answer)

if __name__=="__main__":
    main()