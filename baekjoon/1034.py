"""
    gold5 : 램프
    URL = https://www.acmicpc.net/problem/1034
    dfs문제
"""

import copy

M, N = map(int, input().split())
table = [[0 for col in range(N)] for row in range(M)]

for i in range(0, M):
    tmp = input()
    for j in range(0, N):
        table[i][j] = int(tmp[j])

K = int(input())
sort_table = sorted(table)
max_row_number = 0

for i in range(0, M):
    tmp = 0
    if(i==0):
        tmp = sort_table.count(sort_table[i])
        if( sort_table[i].count(0) <= K and (K - sort_table[i].count(0) ) % 2 == 0 ):
            if(max_row_number < tmp):
                max_row_number = tmp
    else:
        if(sort_table[i-1] == sort_table[i]):
            pass
        else:
            tmp = sort_table.count(sort_table[i])
            if(sort_table[i].count(0) <= K and (K - sort_table[i].count(0) ) % 2 == 0):
                if(max_row_number < tmp):
                    max_row_number = tmp

print(max_row_number)



"""
def find_max_row():
    tmp_sort_table = copy.deepcopy(sort_table)
    del tmp_sort_table[0]
    global same_row 
    

    max_same_row = 0
    for i in sort_table:
        tmp_max_same_row = 1
        for j in tmp_sort_table:
            if(i == j):
                tmp_max_same_row += 1
        
        if(len(tmp_sort_table) != 0):
            del tmp_sort_table[0]
        if(max_same_row < tmp_max_same_row):
            same_row = i
            max_same_row = tmp_max_same_row


max_same_row = find_max_row()
print(same_row)
sort_table.remove(same_row)
print(sort_table)
print(max_same_row)
"""

"""
same_row = table[0][0]
same_row_number = 0 
for i in range(0, M):
    for j in range(0, N):
        if(same_row == table[i][j]):
            same_row_number += 1
"""
