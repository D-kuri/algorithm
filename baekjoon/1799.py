"""
    gold2 : 비숍
    URL = https://www.acmicpc.net/problem/1799
    backtracking
"""

import sys
sys.setrecursionlimit(10**8)
import copy
N = 0
chess = []
bishop = 0
answer = 0
dx , dy = [-1, -1, 1, 1], [-1, 1, -1, 1] #left_up , right_up, left_down, right_down

def duple(x, y, change_num):
    global N, chess

    #chess[x][y] = change_num

    for i in range(4):
        move_x , move_y = x, y
        while 0 <= move_x < N and 0 <= move_y < N:
            chess[move_x][move_y] = change_num

            move_x, move_y = move_x+dx[i], move_y+dy[i]
def solve(x, y):
    global N, chess, bishop, answer
    #print(x,y)
    if y > N-1:
        if y % 2 == 0:
            y = 1
        else:
            y = 0
        solve(x+1, y)
        return 0

    if x == N:
        #print(answer)
        answer = max(answer, bishop)
        return 0
    
    if chess[x][y] == 0:
        solve(x, y+2)
    else:
        original_chess = copy.deepcopy(chess)
        duple(x, y, 0)
        bishop += 1
        solve(x, y+2)

        #duple(x, y, 1)
        chess = original_chess
        bishop -= 1
        solve(x, y+2)

    

def main():
    global N, chess, bishop, answer

    N = int(sys.stdin.readline().strip())

    chess = [[] for _ in range(N)]

    for i in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        chess[i] = row

   
    solve(0, 0)
    tmp = answer
    bishop = 0
    answer = 0 
    solve(0, 1)
    print(tmp+answer)

if __name__ == "__main__":
    main()