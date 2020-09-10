"""
    gold4 : 세 용액
    URL = https://www.acmicpc.net/problem/2473
"""

import sys

N = int(input())
liquid = list(map(int, sys.stdin.readline().strip().split()))
liquid.sort()

close_zero = [10**10, 0,0,0]
for i in range(N-2):
    start , end = i+1 , N-1
    if abs(close_zero[0]) > abs(liquid[i] + liquid[start] + liquid[end]):
        close_zero = [liquid[i] + liquid[start] + liquid[end], i, start, end]

    if close_zero[0] == 0:
        break
    
    #close_zero = [liquid[i] + liquid[start] + liquid[end], i, start, end]
    for j in range(N-2-start):
        if liquid[i] + liquid[start] + liquid[end] < 0: start += 1
        else: end -= 1
        if start == end:
            break
        
        if abs(close_zero[0]) > abs(liquid[i] + liquid[start] + liquid[end]):
            close_zero = [liquid[i] + liquid[start] + liquid[end], i, start, end]
        
        if close_zero[0] == 0:
            break
    

""" print("===================")
print(liquid)
print(close_zero) """
print(liquid[close_zero[1]], liquid[close_zero[2]], liquid[close_zero[3]])
