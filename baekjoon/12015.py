"""
    gold2 : 가장 긴 증가하는 부분수열2
    URL = https://www.acmicpc.net/problem/12015
    LIS (최장 증가 부분수열) 알고리즘
"""

N = int(input())

array = list(map(int, input().split()))
result = []

def lower_bound(arr, num):
    start , end = 0, len(arr)-1

    while(end > start):
        mid = (start + end) // 2
        if arr[mid] >= num:
            end = mid
        else:
            start = mid + 1
    
    arr[end] = num
    return arr

for i in range(N):
    if result == []:
        result.append(array[i])
        continue

    if result[-1] < array[i]:
        result.append(array[i])
    else:
        result = lower_bound(result, array[i])

print(len(result))
