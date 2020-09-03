'''
    Level3 : 이중우선순위큐
    URL = https://programmers.co.kr/learn/courses/30/lessons/42628
'''

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

def solution(operations):
    array = []
    
    for i in range(len(operations)):
        operation, number = operations[i].split()
        if operation == "I":
            array.append(int(number))
            array.sort()
        elif operation == "D" and len(array) != 0:
            index = -1 if int(number) == 1 else 0
            del array[index]
        
    if len(array) == 0:
        answer = [0,0]
    else:
        answer = [array[-1],array[0]]
    return answer

solution(operations)