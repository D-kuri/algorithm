"""
    bronze2 : 최댓값
    URL = https://www.acmicpc.net/problem/2562
"""

def main():
    array = []
    for i in range(9):
        n = int(input())
        array.append([i,n])

    array.sort(key=lambda x:x[1])
    print(array[-1][1])
    print(array[-1][0]+1)

if __name__ == "__main__":
    main()