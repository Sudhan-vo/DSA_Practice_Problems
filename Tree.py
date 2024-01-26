class Node:
    def __init__(self,val):
        self.rootnode=val
        self.leftnode=None
        self.rightnode=None
def preorder(treenode):
    if not treenode:
        return
    print(treenode.rootnode,end=" ")
    preorder(treenode.leftnode)
    preorder(treenode.rightnode)
def inorder(treenode):
    if not treenode:
        return
    inorder(treenode.leftnode)
    print(treenode.rootnode,end=" ")
    inorder(treenode.rightnode)
def postorder(treenode):
    if not treenode:
        return
    postorder(treenode.leftnode)
    postorder(treenode.rightnode)
    print(treenode.rootnode,end=" ")
def levelorder(treenode):
    if not treenode:
        return
    q=[]
    q.append(treenode)
    while q:
        root=q.pop(0)
        print(root.rootnode,end=" ")
        if root.leftnode:
            q.append(root.leftnode)
        if root.rightnode:
            q.append(root.rightnode)
        
root=Node(1)
left=Node(2)
left1=Node(4)
left2=Node(5)
root.leftnode=left
left.leftnode=left1
left.rightnode=left2
right=Node(3)
right1=Node(6)
right2=Node(7)
root.rightnode=right
right.leftnode=right1
right.rightnode=right2
print("preorder:")
preorder(root)
print("\ninorder:")
inorder(root)
print("\npostorder:")
postorder(root)
print("\nlevelorder:")
levelorder(root)