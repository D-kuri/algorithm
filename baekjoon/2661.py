"""
    gold4 : 좋은수열
    URL = https://www.acmicpc.net/problem/2661
"""



n = int(input())

def find_sol(index):
    global seq

    length = len(seq)
    for i in range(0, int(length/2)):
        #print(seq[length-i-1:length], "and", seq[length-i-(i+1)-1:length-i-1])
        if seq[length-i-1:length] == seq[length-i-(i+1)-1:length-i-1]:
            return 1

    if n == index:
        ''' print(seq)
        for i in seq:
            print(i, end='') '''
        return 2

    for i in range(1,4):
        seq.append(i)
        if find_sol(index+1) == 2:
            return 2
        seq.pop()



seq = []
find_sol(0)

for i in seq:
    print(i, end='')


''' 
T = int(input())

seq = ["0"] * 80
seq[6] = "1213121"

def find_sol(n):
    prior_n = seq[n-1]
    half = int((n+1)/2)

    index = 1
    while(1):
        if index%3 == 0:
            index += 1

        tmp = prior_n + str(index)
        #print(tmp)

        check = 0
        for i in range(0,half):
            #print(tmp[n-i:n+1], "and", tmp[n-i-(i+1):n-i])
            if tmp[n-i:n+1] == tmp[n-i-(i+1):n-i]:
                check = 1

        if check == 0:
            seq[n] = tmp
            break
        else:
            index += 1

        break

find_sol(7) '''