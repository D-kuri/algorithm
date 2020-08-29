"""
    gold4 : 문자열 폭발
    URL = https://www.acmicpc.net/problem/9935
    kmp 풀이 + stack (kmp는 시간초과)
"""

string = input()
bomb_string = input()

stack = []
result = ""

for i in range(len(string)):
    stack.append(string[i])

    check = 0
    if len(stack) >= len(bomb_string):
        for j in range(len(bomb_string)):
            if stack[-1-j] != bomb_string[-1-j]:
                check = 1
                break
        
        if check == 0:
            for j in range(len(bomb_string)):
                stack.pop()

for i in stack:
    result += i

if result == "":
    print("FRULA")
else:
    print(result)
''' 
string = input()
bomb_string = input()

pi = [0 for i in range(len(bomb_string))]

def getPi(index):
    global pi

    tmp = 0
    tmp_str = bomb_string[:index+1]
    for i in range(index):
        if bomb_string[:i+1] == tmp_str[len(tmp_str)-1-i:len(tmp_str)]:
            tmp = i+1 if tmp < i+1 else tmp
    pi[index] = tmp



def solve():
    global string, bomb_string

    i=0
    while i < len(string):
        check = 0

        for j in range(len(bomb_string)):
            if string[i+j] != bomb_string[j]:
                check = 1
                if j==0:
                    j=1
                i = i+j - pi[j-1]
                break

        if check == 0 :
            string = string[0:i] + string[i+len(bomb_string):len(string)] #string[i:i+len(bomb_string)]
            break

for i in range(len(bomb_string)):
    getPi(i)

while 1:
    solve()
    if string.find(bomb_string) == -1:
        if string == "":
            print("FRULA")
        else:
            print(string)
        break
 '''



