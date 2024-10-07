class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def top_View_Traversal(node_pos, arr, queue):
    root = queue.pop(0)
    if root is None:
        return
    pos = node_pos[root]
    if arr[pos] == 0:
        arr[pos] = root.info
    node_pos[root.left] = pos - 1
    node_pos[root.right] = pos + 1
    queue.append(root.left)
    queue.append(root.right)

    
def topView(root):
    pos = 500
    arr = []
    for i in range(1000):
        arr.append(0)
    node_pos = {}
    node_pos[root] = pos
    queue = []
    queue.append(root)
    while len(queue) > 0:
        top_View_Traversal(node_pos, arr, queue)
    for i in range(1000):
        if arr[i]!=0:
            print(arr[i], end=" ")



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
