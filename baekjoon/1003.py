"""
    silver3 : 피보나치 함수
    URL = https://www.acmicpc.net/problem/1003
    메모이제이션 문제
"""

T = int(input())
result = []
memory = [0,1]


def fibonacci(i):
    tmp = 0

    if(i < 2):
        tmp = i
    else:
        if(len(memory) >= i+1):
            tmp = memory[i]
        else:
            tmp = fibonacci(i-1)+fibonacci(i-2)
            memory.append(tmp)

    return tmp

for i in range(0,T):
    N = int(input())
    if(N==0):
        result.append([1,0])
    else:
        result.append([fibonacci(N-1), fibonacci(N)])

for i in result:
    print(i[0], i[1])