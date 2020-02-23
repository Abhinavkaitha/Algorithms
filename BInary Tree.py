# https://www.youtube.com/watch?v=YlgPi75hIBc

class Node:
    def __init__(self,val):
        self.value = val
        self.leftchild = None
        self.rightchild = None
    def insert(selfself, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild :
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True
    def find(self, data):
        if (self.value == data):
            return True
        else:

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True