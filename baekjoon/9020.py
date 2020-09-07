"""
    silver1 : 골드바흐의 추측
    URL = https://www.acmicpc.net/problem/9020
    에라토스테네스의 체 (소수 구하는 방법)
"""
import sys

T = int(input())
result = []

numbers = [i for i in range(0,10001)]


for i in range(2, int(10000**0.5)):
    if numbers[i] == 0:
        pass
    else:
        for j in range(2*i, 10000, +i):
            numbers[j] = 0



for i in range(T):
    n = int(sys.stdin.readline().strip())

    tmp_result = []
    for i in range(2, int(n/2)+1):
        if numbers[i] == 0:
            pass
        else:
            if numbers[n-i] != 0:
                if tmp_result == []:
                    tmp_result.append(i)
                    tmp_result.append(n-i)
                    tmp_result.append(abs(n-(2*i)))
                else:
                    if tmp_result[2] > abs(n-(2*i)):
                        tmp_result = []
                        tmp_result.append(i)
                        tmp_result.append(n-i)
                        tmp_result.append(abs(n-(2*i)))
    
    result.append([tmp_result[0], tmp_result[1]])

for i in result:
    print(i[0], i[1])