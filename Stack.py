class Stack():
    def __init__(self):
        self.items = []
    def pop(self):
        self.items.pop()
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return self.items == []
    def get_stack(self):
        return self.items

s = Stack()
s.push(2)
print(s.peek())





