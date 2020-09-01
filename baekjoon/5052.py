"""
    gold4 : 전화번호 목록
    URL = https://www.acmicpc.net/problem/5052
    Trie 알고리즘
"""

# python에서 제공하는 startwidth() 사용시 바로 풀림. ()안에 들어간 문자열로 시작하는지를 확인하는 함수.
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, key, data=False):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for char in word:
            if cur.data == True:
                return False
            if char not in cur.child:
                cur.child[char] = Node(char)
            cur = cur.child[char]

            

        cur.data = True
    
    def search(self, word):
        cur = self.head

        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        
        return True
        """ if cur.data == True:
            return True
        else:
            return False """


T = int(sys.stdin.readline().strip())

result = []
for i in range(T):
    n = int(sys.stdin.readline().strip())

    trie = Trie()

    check = 0
    for j in range(n):
        number = sys.stdin.readline().strip()
        #print(type(number), number)
        if check == 0:
            if trie.search(number) == True or trie.insert(number) == False :
                check = 1

        
    if check == 1:
        result.append("NO")
    else:
        result.append("YES")

for i in result:
    print(i)


