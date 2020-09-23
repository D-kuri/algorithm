"""
    gold4 : 플로이드
    URL = https://www.acmicpc.net/problem/11404
    플로이드와샬
"""
import sys

def main():
    N = int(sys.stdin.readline().strip())
    M = int(sys.stdin.readline().strip())

    matrix = [[10**8 for col in range(N)] for row in range(N)]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().strip().split())

        a,b = a-1,b-1
        if matrix[a][b] > c:
            matrix[a][b] = c
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 10**8:
                print(0, end=" ")
            else:
                print(matrix[i][j], end=" ")
        print()

if __name__=="__main__":
    main()