"""
    gold4 : 수 묶기
    URL = https://www.acmicpc.net/problem/1744
    그냥 수학문제
"""

N = int(input())

array = []
array_positive = []
array_negative =  []

for i in range(N):
    number = int(input())
    if number > 0:
        array_positive.append(number)
    else:
        array_negative.append(number)


array_positive.sort(reverse=True)
array_negative.sort()
array.extend(array_positive)
array.extend(array_negative)

i=0
result = 0
while i < N:
    if i == N-1:
        result += array[i]
        break
    elif array[i] * array[i+1] > array[i] + array[i+1]:
        result += array[i] * array[i+1]
        i += 2
    else:
        result += array[i]
        i += 1

print(result)