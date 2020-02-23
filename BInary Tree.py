class Node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None



class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)




class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

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
        elif traversal_type == 'levelorder':
            return self.level_order_print(tree.root)
        elif traversal_type == 'reverselevelorder':
            return self.reverse_level_order(tree.root)

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

    def level_order_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue)>0:

            current_node = queue.dequeue()
            traversal = traversal + '-' + str(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
        return traversal

    def reverse_level_order(self, start):

        if start is None:
            return
        queue = Queue()
        stack = Stack()

        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            current_node = queue.dequeue()
            stack.push(current_node)
            if current_node.right:
                queue.enqueue(current_node.right)
            if current_node.left:
                queue.enqueue(current_node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal = traversal+str(node.value)+"-"
        return traversal

    def height(self,node):

        if not node:
            return -1
        L = self.height(node.left)
        R = self.height(node.right)

        return 1+max(L,R)

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

print('Pre Order ',tree.print_tree("preorder"))
print('In Order ', tree.print_tree("inorder"))
print('Post Order ', tree.print_tree("postorder"))
print('Level Order ', tree.print_tree('levelorder'))
print('Reverse Level Order ', tree.print_tree('reverselevelorder'))
print(tree.height(tree.root))

