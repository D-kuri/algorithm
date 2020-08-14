"""
    silver4 : 터렛
    URL = https://www.acmicpc.net/problem/1002
    두 원 접점의 개수 문제
"""
import math

Testcate = int(input())

result = []

def calc_result(d, r1, r2):
    if(r1+r2 == d or abs(r1-r2) == d):
        return 1
    elif(r1+r2 < d or abs(r1-r2) > d):
        return 0
    elif(abs(r1-r2) < d and r1+r2 > d):
        return 2

for i in range(0, Testcate):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if(x1 == x2 and y1 == y2 and r1 == r2):
        result.append(-1)
    else:
        d = math.sqrt(pow(x1-x2,2) + pow(y1-y2,2))
        tmp = calc_result(d, r1, r2)
        result.append(tmp)

for i in result:
    print(i)

