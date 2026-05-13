class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return self.data
        
root = Node("A") 
root.left = Node("B")  
root.right =Node("C")  

root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")

def inoder(node):
    if node:
        inoder(node.left)
        print(node.data,end="->")
        inoder(node.right)
print("Reading the data from Tree Inorder")
print(f" {inoder(root)}")

def preorder(node):
    if node:
        print(node.data,end="->")
        preorder(node.left)
        preorder(node.right)
print("Reading the data in Preorder :")
print(f"{preorder(root)} ")

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end="->")
print("Reading the data in Post Order :")
print(f" {postorder(root)}")
