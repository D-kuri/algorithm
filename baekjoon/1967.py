"""
    gold4 : 트리의 지름
    URL = https://www.acmicpc.net/problem/1967
    DFS + Tree
"""
import sys
sys.setrecursionlimit(10**6)
max_dia = 0
max_dia_list = []
array = []
visited = []
stack = []
answer = 0

class Node(object):
    def __init__(self, data, cost=0):
        self.data = data
        self.cost = cost
        self.children = []
    
    def insert(self, node):
        self.children.append(node)

def preorder(node, dia, root_data):
    global max_dia, max_dia_list

    if node.data != root_data:
        dia += node.cost
    #print(node.data,   end="-")
    if not node.children:
        max_dia_list.append([dia, node.data])
        if dia > max_dia:
            max_dia = dia

    for i in node.children:
        preorder(i, dia, root_data )
        #print(max_dia)
        max_dia = 0

def find_parent_list(parent_list, index):
    global array
    if parent_list[index]:
        array.append(parent_list[index][0])
        find_parent_list(parent_list, parent_list[index][0])

def dfs(edge_list):
    global visited, stack, answer

    if not stack:
        return 0
    index = stack.pop(0)
    if index[1] > answer:
        answer = index[1]
    visited[index[0]] = True
    for i in edge_list[index[0]]:
        if visited[i[0]] == False:
            stack.append([i[0], i[1]+index[1]])
    dfs(edge_list)


def main():
    global max_dia, array, max_dia_list, visited, stack

    N = int(sys.stdin.readline().strip())

    node_list = [Node(i) for i in range(1, N+1)]
    parent_list = [[] for _ in range(N+1)]
    edge_list = [ [] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for i in range(N-1):
        parent, child, cost = map(int,sys.stdin.readline().strip().split())
        parent_list[child].append(parent)
        edge_list[parent].append([child, cost])
        edge_list[child].append([parent, cost])

        node_list[child-1].cost = cost
        node_list[parent-1].insert(node_list[child-1])
    #print(edge_list)
    dia = 0
    preorder(node_list[0], dia, node_list[0].data)

    max_dia_list.sort(key=lambda x:x[0])
    find_parent_list(parent_list, max_dia_list[-1][1])
    index = max_dia_list[-1][1]

    #visited[index] = True
    stack.append([index, 0])
    dfs(edge_list)
    print(answer)



if __name__ == "__main__":
    main()


""" 
import sys
sys.setrecursionlimit(10**6)
max_dia = 0
max_dia_list = []
check_dia = []

class Node(object):
    def __init__(self, data, cost=0):
        self.data = data
        self.cost = cost
        self.children = []
    
    def insert(self, node):
        self.children.append(node)

def preorder(node, dia, root_data):
    global max_dia, check_dia

    if node.data != root_data:
        dia += node.cost
    #print(node.data,   end="-")
    if not node.children:
        #print(dia)
        if dia > max_dia:
            max_dia = dia

    for i in node.children:
        preorder(i, dia, root_data)
        if node.data == root_data:
            #print(max_dia)
            check_dia.append(max_dia)
            max_dia = 0



def main():
    global max_dia, check_dia

    N = int(sys.stdin.readline().strip())

    node_list = [Node(i) for i in range(1, N+1)]
    for i in range(N-1):
        parent, child, cost = map(int,sys.stdin.readline().strip().split())

        node_list[child-1].cost = cost
        node_list[parent-1].insert(node_list[child-1])

    answer = 0
    for i in range(N):    
        dia = 0
        check_dia = []
        preorder(node_list[i], dia, node_list[i].data)
        check_dia.sort(reverse=True)
        max_ = 0
        if len(check_dia) == 1:
            max_ = check_dia[0]
        elif len(check_dia) > 1:
            max_ = check_dia[0] + check_dia[1]

        if answer < max_:
            answer = max_
        #print(check_dia, sum(check_dia))
    print(answer)



if __name__ == "__main__":
    main() """