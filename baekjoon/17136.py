"""
    gold2 : 색종이붙이기
    URL = https://www.acmicpc.net/problem/17136
    백트래킹
"""

import sys
import copy
sys.setrecursionlimit(10**8)
matrix = []
answer = sys.maxsize
paper_num = [5 for _ in range(6)]
def check(x, y):
    global paper_num, answer, matrix

    if y == 10:
        check(x+1, 0)
        return 0

    if x == 10:
        answer = min(answer, 30-sum(paper_num))
        return 0
        
    if matrix[x][y] == '0':
        check(x, y+1)

    for n in range(5, 0, -1):
        if paper_num[n]==0 or x+n > 10 or y+n > 10:
            continue

        all_n = True
        for i in range(x, x+n):
            for j in range(y, y+n):
                if matrix[i][j] == '0':
                    all_n = False
                    break
            if not all_n:
                break
        
        if not all_n:
            continue
        
        paper_num[n] -= 1
        for i in range(x, x+n):
            for j in range(y, y+n):
                matrix[i][j] = '0'
        check(x, y+n)

        paper_num[n] += 1
        for i in range(x, x+n):
            for j in range(y, y+n):
                matrix[i][j] = '1'


    

def main():
    global answer, matrix

    for _ in range(10):
        row = sys.stdin.readline().strip().split()
        matrix.append(row)

    check(0, 0)
    if answer == sys.maxsize:
        print(-1)
    else:
        print(answer)
    
if __name__ == "__main__":
    main()