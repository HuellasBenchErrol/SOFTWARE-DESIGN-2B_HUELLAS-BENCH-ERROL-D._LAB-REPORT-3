class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key




def Inorder(root):
    if root:
        Inorder(root.left)

        print(root.val)

        Inorder(root.right)


def Postorder(root):
    if root:
        Postorder(root.left)

        Postorder(root.right)

        print(root.val)


def Preorder(root):
    if root:
        print(root.val)

        Preorder(root.left)

        Preorder(root.right)


root = Node(2)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(10)


print("Preorder traversal of binary tree is")
Preorder(root)

print("\nInorder traversal of binary tree is")
Inorder(root)

print("\nPostorder traversal of binary tree is")
Postorder(root)
