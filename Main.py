class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    # if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(new_value)
        return root

    # binary search tree is not empty, so we will insert it into the tree
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if new_value < root.data:
        root.left_child = insert(root.left_child, new_value)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.right_child = insert(root.right_child, new_value)
    return root


def inorder(root) -> None:
    # Write your code here
    # if root is None,return
    if root is None:
        return
    # traverse left subtree
    inorder(root.left_child)
    # traverse current node
    print(root.data, end=' ')
    # traverse right subtree
    inorder(root.right_child)


def preorder(root) -> None:
    # Write your code here
    # if root is None return
    if root is None:
        return
    # traverse root
    print(root.data, end=' ')
    # traverse left subtree
    preorder(root.left_child)
    # traverse right subtree
    preorder(root.right_child)    


def postorder(root) -> None:
    # Write your code here
    # if root is None return
    if root is None:
        return
    # traverse left subtree
    postorder(root.left_child)
    # traverse right subtree
    postorder(root.right_child)
    # traverse root
    print(root.data, end=' ')    


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
