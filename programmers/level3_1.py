"""
    Level3 : 자물쇠와 열쇠
    URL = https://programmers.co.kr/learn/courses/30/lessons/60059
    *2020 kakao blind recruitment
"""

key = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]
lock = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
import copy

def rotate(key):
    m = len(key)

    tmp_key = [[0 for col in range(m)] for row in range(m)]
    for i in range(m):
        for j in range(m):
            tmp_key[j][m-1-i] = key[i][j]

    return tmp_key

def unlock(key, lock):
    m = len(key)
    n = len(lock)

    tmp_array = [ [0 for col in range(n+2*m-2)] for row in range(n+2*m-2)]

    for i in range(m-1, n+m-1):
        for j in range(m-1, n+m-1):
            tmp_array[i][j] = lock[i-m+1][j-m+1]



    check = 0
    for i in range(len(tmp_array)-m+1):
        for j in range(len(tmp_array)-m+1):
            comp_array = copy.deepcopy(tmp_array)
            for k in range(m):
                for l in range(m):
                    comp_array[i+k][j+l] = key[k][l] ^ tmp_array[i+k][l+j]
            
            all_pass = 1
            for k in range(m-1, n+m-1):
                for l in range(m-1, n+m-1):
                    if comp_array[k][l] == 0:
                        all_pass = 0
            
            if all_pass == 1:
                check = 1

    
    if check == 1:
        return 1
    else:
        return 0

def solution(key, lock):
    m = len(key)
    n = len(lock)

    answer = False

    all_unlock = 0
    for i in lock:
        if i.count(1) == n:
            all_unlock += 1

    if all_unlock == n:
        answer = True
    else:
        for i in range(1):
            result = unlock(key, lock)
            print(result)
            if result == 1:
                answer = True
                break

            key = rotate(key)

    return answer

solution(key, lock)