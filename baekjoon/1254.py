"""
    silver1 : 팰린드롬 만들기
    URL = https://www.acmicpc.net/problem/1254
"""

S = input()
reverse_S = S[::-1]
lcs = 0
result = 0

while(1):
    tmp = len(S)+result
    check_even = (len(S)+result) % 2
    if(check_even == 0):
        check = 0
        for i in range(len(S[int(tmp/2):][::-1])):
            if(S[int(tmp/2):][::-1][i] != S[0:int(tmp/2)][i+result]):
                check = 1
                break
        if(check == 0):
            break
        result += 1
    else:
        check = 0
        for i in range(len(S[int(tmp/2)+1:][::-1])):
            if(S[int(tmp/2)+1:][::-1][i] != S[0:int(tmp/2)][i+result]):
                check = 1
                break
        if(check == 0):
            break
        result += 1

print(result+len(S))




"""
두 문자 공통으로 가지고 있는 문자열 찾기
for i in range(len(S)):
    tmp = ""
    for j in range(len(S)):
        next_point = 0
        if(S[i] == reverse_S[j] and j+next_point < len(S)):
            while(j+next_point < len(S)):
                next_point += 1
                if(S[i:i+next_point+1] == reverse_S[j:j+next_point+1] and j+next_point < len(S)):
                    pass
                else:
                    if(lcs < len(S[i:i+next_point])):
                        lcs = len(S[i:i+next_point])
                    break

print(2*len(S)-lcs)
"""