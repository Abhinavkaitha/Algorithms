class Node:

    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class Tree:

    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.pre_order_print(tree.root, "")
        elif traversal_type == 'inorder':
            return self.in_order_print(tree.root, "")
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, "")

    def pre_order_print(self, start, traversal):
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal = self.in_order_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


    # def insert(self, data):
    #
    #     if self.root:
    #         return self.root.insert(data)
    #     else:
    #         self.root = Node(data)
    #         return True

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

# Set up tree:
tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))

