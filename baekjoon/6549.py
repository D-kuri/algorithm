"""
    platinum5 : 히스토그램에서 가장 큰 직사각형
    URL = https://www.acmicpc.net/problem/6549
    분할정복
"""
import sys

sys.setrecursionlimit(10**7)

T = []
result = []
max_area = 0


def find_area(start, end, heights):
    global max_area

 
    """ print("------------------")
    print(heights[start:end])
    print(start, end)   """


    min_index = heights[start:end].index(min(heights[start:end])) + start
    width = end-start 
    height = heights[min_index]
    #height = min(heights[start:end])
    
    if max_area < width*height:
        max_area = width*height

    if width == 1:
        return 
    
    #min_index = heights[start:end].index(min(heights[start:end])) + start
    if heights[start:min_index] != []:
        find_area(start, min_index, heights)
    else:
        find_area(start, start+1, heights)

    if heights[min_index+1:end] != []:
        find_area(min_index+1, end, heights)
    else:
        find_area(min_index, end, heights)




while(1):
    T = list(map(int,input().split()))

    n = T[0]
    if n==0:
        break
    max_area = 0
    find_area(0, len(T)-1, T[1:len(T)])
    #print(max_area)
    result.append(max_area)

#print("-----------------")

for i in result:
    print(i)


''' 
T = []
result = []
max_area = 0

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Tree:
    def createNode(self, data):
        return node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            node.next = self.insert(node.next, data)
        
        return node

def find_area(heights):
    if heights == []:
        return 0
    width = len(heights) 
    height = min(heights)
    return width * height


def make_tree(root, heights):
    if(len(heights) != 2):
        index = heights.index(min(heights))
        left_heights = heights[0:index]
        right_heights = heights[index+1:len(heights)]
    elif len(heights) == 2:
        left_heights = [heights[0]]
        right_heights = [heights[1]]
    else:
        return root

    
    tree = Tree()
    root = tree.insert(root, left_heights)
    root = tree.insert(root, right_heights)

    


    if len(left_heights) == 1 or len(left_heights) == 0:
        #print(111)
        pass
    else:
        #print(222)
        root = make_tree(root, left_heights)

    if len(right_heights) == 1 or len(right_heights) == 0:
        #print(333)
        pass
    else:
        #print(444)
        root = make_tree(root, right_heights)

    return root

def preorder(node):
    global max_area

    if node is None:
        return
    #print(node.data)
    tmp = find_area(node.data)
    #
    # print(tmp)
    if(max_area < tmp):
        max_area = tmp
    preorder(node.next)

while(1):
    T = list(map(int,input().split()))

    n = T[0]
    if n==0:
        break
    max_area = 0
    #print(min(T))
    #print(T.index(min(T)))

    root = None
    tree = Tree()
    root = tree.insert(root, T[1:len(T)])
    root = make_tree(root, T[1:len(T)])
    preorder(root)
    #print(max_area)
    result.append(max_area)

for i in result:
    print(i)
 '''