"""
    gold5 : N-Queen
    URL = https://www.acmicpc.net/problem/9663
    백트래킹
"""

import sys
sys.setrecursionlimit(10**8)
answer = 0
N = 0

def backtracking(chess, x):
    global answer, N

    for i in range(x):
        if chess[i] == chess[x] or abs(chess[i]-chess[x]) == abs(i-x):
            return 0
    
    if x == N-1:
        answer += 1
        return 

    for i in range(N):
        chess[x+1] = i
        backtracking(chess, x+1)


def main():
    global N, answer

    N = int(sys.stdin.readline().strip())

    chess = [-1 for _ in range(N)]

    for i in range(N):
        chess[0] = i

        backtracking(chess, 0)
    
    print(answer)

if __name__ == "__main__":
    main()
