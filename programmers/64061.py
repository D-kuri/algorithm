"""
    Level2 : 크레인 인형뽑기 게임
    URL = https://programmers.co.kr/learn/courses/30/lessons/64061
    *2019 카카오 개발자 겨울 인턴십 
    level2
"""

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    a = [[] for i in range(len(board))]
    result = []
    answer = 0

    length = len(board)
    for i in range(length):
        for j in range(length):
            if(board[i][j] != 0):
                a[j].append(board[i][j])

    moves.reverse()
    for i in range(len(moves)):
        move_tmp = moves.pop()-1
        if(len(result) >= 1):
            for j in range(len(a[move_tmp])):
                result.append(a[move_tmp][j])
                del a[move_tmp][j]
                break
            if(result[len(result)-1] == result[len(result)-2]):
                result.pop()
                result.pop()
                answer += 2
        else:
            for j in range(len(a[move_tmp])):
                result.append(a[move_tmp][j])
                del a[move_tmp][j]
                break

    return answer

solution(board,moves)