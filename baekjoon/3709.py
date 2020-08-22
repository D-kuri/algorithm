"""
    gold4 : 레이저빔은 어디로
    URL = https://www.acmicpc.net/problem/3709
    시뮬레이션
"""
T = int(input())

up = [-1,0]
down = [1,0]
left = [0, -1]
right = [0, 1]
check_inf = 0
result = []

def lazer_box(direction, now_position, borad):
    global up, down, left, right, check_inf
    check_inf += 1
    if(check_inf > 2500):
        return [0,0] 

    if(now_position[0] == len(board) or now_position[0] < 0 or now_position[1] == len(board) or now_position[1] < 0): #len(board) is n
        return [now_position[0]+1,now_position[1]+1]

    if(borad[now_position[0]][now_position[1]] == 0):
        return lazer_box(direction, [now_position[0]+direction[0], now_position[1]+direction[1]], board)
    else:
        if(direction == up): #rotate right
            direction = right
            return lazer_box(direction, [now_position[0]+direction[0], now_position[1]+direction[1]], board)
        elif(direction == down): #rotate left
            direction = left
            return lazer_box(direction, [now_position[0]+direction[0], now_position[1]+direction[1]], board)
        elif(direction == left): #rotate up
            direction = up
            return lazer_box(direction, [now_position[0]+direction[0], now_position[1]+direction[1]], board)
        elif(direction == right): #rotate down
            direction = down
            return lazer_box(direction, [now_position[0]+direction[0], now_position[1]+direction[1]], board)
        


for i in range(T):
    n, r = map(int, input().split())

    board = [[0 for col in range(n)] for row in range(n)]

    for j in range(r):
        x, y = map(int, input().split())
        board[x-1][y-1] = 1
    
    lazer_x, lazer_y = map(int, input().split())

    
    if(lazer_x > n): #up
        result_tmp = lazer_box(up, [lazer_x-1+up[0], lazer_y-1+up[1]], board)
    elif(lazer_x < 1): #down
        result_tmp = lazer_box(down, [lazer_x-1+down[0], lazer_y-1+down[1]], board)
    elif(lazer_y > n): #left
        result_tmp = lazer_box(left, [lazer_x-1+left[0], lazer_y-1+left[1]], board)
    elif(lazer_y < 1): #right
        result_tmp = lazer_box(right, [lazer_x-1+right[0], lazer_y-1+right[1]], board)



    result.append(result_tmp)

for i in result:
    print(i[0], i[1])
