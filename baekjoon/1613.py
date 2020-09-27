"""
    gold3 : 역사
    URL = https://www.acmicpc.net/problem/1613
    플로이드와샬
"""
import sys

def main():
    N, K = map(int, sys.stdin.readline().strip().split())

    history = [[10**8 for col in range(N)] for row in range(N)]

    
    for _ in range(K):
        before, after = map(int, sys.stdin.readline().strip().split())

        before, after = before-1, after-1
        history[before][after] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j and history[i][k] == 1 and history[k][j] == 1:
                    history[i][j] = 1
    
    for i in history:
        print(i)
    S = int(sys.stdin.readline().strip())

    answer = []
    for _ in range(S):
        q1, q2 = map(int, sys.stdin.readline().strip().split())

        q1, q2 = q1-1, q2-1
        if history[q1][q2] != 10**8:
            print("-1")
        elif history[q2][q1] != 10**8:
            print("1")
        else:
            print("0")
    

if __name__=="__main__":
    main()

'''     
import sys

def main():
    N, K = map(int, sys.stdin.readline().strip().split())

    history = [[10**8 for col in range(N)] for row in range(N)]

    
    for _ in range(K):
        before, after = map(int, sys.stdin.readline().strip().split())

        before, after = before-1, after-1
        history[before][after] = 1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j and history[i][j] > history[i][k] + history[k][j]:
                    history[i][j] = history[i][k] + history[k][j]
    
    S = int(sys.stdin.readline().strip())

    answer = []
    for _ in range(S):
        q1, q2 = map(int, sys.stdin.readline().strip().split())

        q1, q2 = q1-1, q2-1
        if history[q1][q2] != 10**8:
            print("-1")
        elif history[q2][q1] != 10**8:
            print("1")
        else:
            print("0")
    

if __name__=="__main__":
    main() '''