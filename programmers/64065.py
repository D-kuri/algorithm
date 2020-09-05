"""
    Level2 : tuple
    URL = https://programmers.co.kr/learn/courses/30/lessons/64065
    *2019 카카오 개발자 겨울 인턴십 
    level2
"""

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

def solution(s):
    s = s[1:-1]
    answer = []

    for i in range(len(s)):
        if(s[i] =="}"):
            s = s[:i+1] + "." + s[i+2:]

    s = s[:-1]
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.split(".")


    for i in range(len(s)):
        s[i] = s[i].split(",")
        for j in range(len(s[i])):
            s[i][j] = int(s[i][j])


    s.sort()
    for i in range(len(s)):
        if(i == 0):
            answer.append(s[i][0])
        else:
            for j in range(len(answer)):
                s[i].remove(answer[j])
            answer.append(s[i][0])

    return answer

solution(s)