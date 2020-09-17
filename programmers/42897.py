"""
    Level2 : 도둑질
    URL = https://programmers.co.kr/learn/courses/30/lessons/42987
    DP
"""

def solution(money):
    N = len(money)
    house = [ 0 for _ in range(N) ]

    house[0] = money[0]
    house[1] = max(money[0], money[1])
    for i in range(2, N-1):
        house[i] = max(money[i] + house[i-2], house[i-1])

    house2 = [ 0 for _ in range(N) ]
    house2[1] = money[1]
    for i in range(2, N):
        house2[i] = max(money[i] + house2[i-2], house2[i-1])

    print(house)
    print("----------")
    print(house2)
    answer = max(max(house), max(house2))
    return answer

money = [5, 1, 1, 5, 1]
solution(money)