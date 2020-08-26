"""
    gold4 : 고층 건물
    URL = https://www.acmicpc.net/problem/1027
    수학문제
"""

N = int(input())
height = list(map(int,input().split()))

building = []
max_view = 0
left_view = 0
right_view = 0

for i in range(N):
    building.append([i, height[i]])

def left_check(now_building, left_building, gradient): #gradient init is + 10 ** 10
    global building, left_view
    if(left_building < 0):
        return 0
    else:
        tmp_gradient = (building[now_building][1] - building[left_building][1]) / (building[now_building][0] - building[left_building][0])
        if(gradient > tmp_gradient):
            gradient = tmp_gradient
            left_view += 1
        left_check(now_building, left_building-1, gradient)
    
    

def right_check(now_building, right_building, gradient): #gradient init is - 10 ** 10
    global building, right_view
    if(right_building > N-1):
        return 0
    else:
        tmp_gradient = (building[now_building][1] - building[right_building][1]) / (building[now_building][0] - building[right_building][0])
        if(gradient < tmp_gradient):
            gradient = tmp_gradient
            right_view += 1
        right_check(now_building, right_building+1, gradient)
    
    

for i in range(N):
    left_view, right_view = 0, 0

    left_check(i, i-1, 10**10)
    right_check(i, i+1, -(10**10))

    if(left_view+right_view > max_view):
        max_view = left_view + right_view

print(max_view)