"""
    Level3 : 길찾기 게임
    URL = https://programmers.co.kr/learn/courses/30/lessons/42892
    2019 KAKAO BLIND RECRUITMENT
"""

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

import sys
sys.setrecursionlimit(10**6)

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def createNode(self, data):
        return node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        elif data[0] < node.data[0]:
            node.left = self.insert(node.left, data)
        elif data[0] > node.data[0]:
            node.right = self.insert(node.right, data)

        return node

def preorder(node, answer):
    if node is None:
        return 
    answer[0].append(node.data[2])
    #print(node.data[2], end="-")
    preorder(node.left, answer)
    preorder(node.right, answer)

def postorder(node, answer):
    if node is None:
        return 
    postorder(node.left, answer)
    postorder(node.right, answer)
    answer[1].append(node.data[2])
    #print(node.data[2], end="-")

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    nodeinfo.sort(key=lambda x:(x[1],x[0]))
    nodeinfo = list(reversed(nodeinfo))
    print(nodeinfo)

    root = None
    tree = Tree()
    root = tree.insert(root, nodeinfo[0])
    for i in range(1, len(nodeinfo)):
        tree.insert(root, nodeinfo[i])
    #print(root.right.data)
    answer = [[]]

    preorder(root, answer)
    answer.append([])
    postorder(root, answer)
    #print(answer)


    return answer

solution(nodeinfo)
