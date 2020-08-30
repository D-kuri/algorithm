'''
    Level3 : 야근지수
    URL = https://programmers.co.kr/learn/courses/30/lessons/12927
'''

works = [4,3,3]
n = 4

def solution(n, works):
    answer = 0

    if sum(works) <= n:
        pass
    else:
        works.sort(reverse=True)
        
        for i in range(n):
            works[works.index(max(works))] = max(works)-1

        for i in works:
            answer += i ** 2


    return answer


solution(n, works)


"""
효율성 검사 통과 x
def solution(n, works):
    answer = 0

    if sum(works) <= n:
        pass
    else:
        for i in range(n):
            works[works.index(max(works))] = max(works)-1

        for i in works:
            answer += i ** 2


    return answer


solution(n, works)
"""