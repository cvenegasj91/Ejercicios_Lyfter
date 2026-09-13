class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def print_structure(self, node):
        if node is None:
            return

        print(node.data)

        self.print_structure(node.left)
        self.print_structure(node.right)


tree = BinaryTree(Node(10))

tree.root.left = Node(8)
tree.root.right = Node(9)

tree.root.left.left = Node(6)
tree.root.left.right = Node(4)

tree.root.right.left = Node(7)
tree.root.right.right = Node(5)

tree.print_structure(tree.root)