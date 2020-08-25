"""
    gold5 : 옥상 정원 꾸미기
    URL = https://www.acmicpc.net/problem/6198
    시뮬레이션
"""

N = int(input())

building = []
result = 0

for i in range(N):
    h = int(input())

    loop = len(building) 
    for j in range(loop):
        if(building[-1] <= h):
            building.pop()
        else:
            break

    result += len(building)    

    building.append(h)

print(result)

''' 
N = int(input())

building = []

def count_view(index):
    global building

    tmp = building[index]
    count = 0
    print("---------------")
    print(index)
    for i in range(index+1, len(building)):
        print(i)
        if(building[i] < tmp):
            count += 1
        else:
            break
    
    return count

for i in range(N):
    h = int(input())

    building.append(h)


result = 0
for i in range(N):
    result += count_view(i)

print(result) 
'''