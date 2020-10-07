"""
    gold1 : 가장 긴 증가하는 부분수열5
    URL = https://www.acmicpc.net/problem/14003
    LIS (최장 증가 부분수열) 알고리즘 // 추적하기 위해 trace 기법 사용
"""

N = int(input())

array = list(map(int, input().split()))
result = []
trace = []

def lower_bound(arr, num):
    start , end = 0, len(arr)-1

    while(end > start):
        mid = (start + end) // 2
        if arr[mid] >= num:
            end = mid
        else:
            start = mid + 1
    
    arr[end] = num
    return arr, [end, num]

for i in range(N):
    if result == []:
        result.append(array[i])
        trace.append([i, array[i]])
        continue

    if result[-1] < array[i]:
        result.append(array[i])
        trace.append([len(result)-1, array[i]])
    else:
        result, tmp = lower_bound(result, array[i])
        trace.append(tmp)


print(len(result))

answer = ""
cnt = len(result)-1
for i in range(len(trace)-1, -1, -1):
    if trace[i][0] == cnt:
        answer = str(trace[i][1]) + " " + answer
        cnt -= 1
print(answer)
