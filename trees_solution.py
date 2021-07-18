class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newValue):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,newValue)
    return root





# TEST CASES
root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
a1=root
a2=a1.leftChild
a3=a1.rightChild
a4=a2.leftChild
a5=a2.rightChild
a6=a3.leftChild
a7=a3.rightChild

print(f"Root Node is: {a1.data}")
print(f"left child of node is: {a1.leftChild.data}")
print(f"right child of node is: {a1.rightChild.data}")
print()
print(f"Node is: {a2.data}")
print(f"left child of node is: {a2.leftChild.data}")
print(f"right child of node is: {a2.rightChild.data}")
print()
print(f"Node is: {a3.data}")
print(f"left child of node is: {a3.leftChild.data}")
print(f"right child of node is: {a3.rightChild.data}")
print()
print(f"Node is: {a4.data}")
print(f"left child of node is: {a4.leftChild}")
print(f"right child of node is: {a4.rightChild}")
print()
print(f"Node is: {a5.data}")
print(f"left child of node is: {a5.leftChild}")
print(f"right child of node is: {a5.rightChild}")
print()
print(f"Node is: {a6.data}")
print(f"left child of node is: {a6.leftChild}")
print(f"right child of node is: {a6.rightChild}")
print()
print(f"Node is: {a7.data}")
print(f"left child of node is: {a7.leftChild}")
print(f"right child of node is: {a7.rightChild}")
