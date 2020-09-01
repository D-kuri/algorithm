"""
    gold4 : 미친 아두이노
    URL = https://www.acmicpc.net/problem/8972
    시뮬레이션
"""

R, C = map(int, input().split())

board = [ [0 for col in range(C)] for row in range(R) ]
arduino = []
mad_arduino = []

for i in range(R):
    input_str = input()
    
    for j in range(len(input_str)):
        tmp = input_str[j]
        if tmp == ".":
            pass
        elif tmp == "R":
            mad_arduino.append([i,j])
            board[i][j] = 1
        else:
            arduino.append(i)
            arduino.append(j)
            board[i][j] = -1

move = input()

up = [-1,0]
left_up = [-1,-1]
right_up = [-1,1]
left = [0,-1]
right = [0,1]
down = [1,0]
left_down = [1,-1]
right_down = [1,1]

def move_arduino(number):
    global up, left_up, left_down, left, right, down, left_down, right_down
    if number == 1:
        return left_down
    elif number == 2:
        return down
    elif number == 3:
        return right_down
    elif number == 4:
        return left
    elif number == 5:
        return [0,0]
    elif number == 6:
        return right
    elif number == 7:
        return left_up
    elif number == 8:
        return up
    elif number == 9:
        return right_up

def move_madarduino(mad_arduino, arduino):
    global up, left_up, left_down, left, right, down, left_down, right_down

    if mad_arduino[0] > arduino[0] and mad_arduino[1] < arduino[1]:
        return right_up #left down
    elif mad_arduino[0] > arduino[0] and mad_arduino[1] == arduino[1]:
        return up #down
    elif mad_arduino[0] > arduino[0] and mad_arduino[1] > arduino[1]:
        return left_up #right_down
    elif mad_arduino[0] == arduino[0] and mad_arduino[1] < arduino[1]:
        return right #left
    elif mad_arduino[0] == arduino[0] and mad_arduino[1] > arduino[1]:
        return left #right
    elif mad_arduino[0] < arduino[0] and mad_arduino[1] < arduino[1]:
        return right_down #left_up
    elif mad_arduino[0] < arduino[0] and mad_arduino[1] == arduino[1]:
        return down
    elif mad_arduino[0] < arduino[0] and mad_arduino[1] > arduino[1]:
        return left_down

X = 0
a=0
for i in range(len(move)):
        """ if int(move[i]) != 5:
            X += 1 """
        moving = move_arduino(int(move[i]))
        
        board[arduino[0]][arduino[1]] += 1
        arduino[0] += moving[0]
        arduino[1] += moving[1]

        board[arduino[0]][arduino[1]] += -1

        if board[arduino[0]][arduino[1]] == 0:
            X = i+1
            break
        
        check = 0
        for j in range(len(mad_arduino)):
            moving_madarduino = move_madarduino(mad_arduino[j], arduino)

            board[mad_arduino[j][0]][mad_arduino[j][1]] += -1
            mad_arduino[j][0] += moving_madarduino[0]
            mad_arduino[j][1] += moving_madarduino[1]

            board[mad_arduino[j][0]][mad_arduino[j][1]] += 1

            if board[mad_arduino[j][0]][mad_arduino[j][1]] == 0:
                check = 1
                break

        for j in range(R):
            for k in range(C):
                if board[j][k] > 1:
                    board[j][k] = 0
                    for w in range(mad_arduino.count([j,k])):
                        mad_arduino.remove([j,k]) 

        if check == 1:
            X = i+1
            break

if X != 0:
    print("kraj " + str(X))
else:
    for i in range(R):
        for j in range(C):
            tmp = board[i][j]
            if tmp == 0:
                board[i][j] = "."
            elif tmp == 1:
                board[i][j] = "R"
            else:
                board[i][j] = "I"

    for i in board:
        print(''.join(i))
        



