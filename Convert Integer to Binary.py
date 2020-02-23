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

def int_to_binary(n):
    s = Stack()
    while n!=0 :
        remainder = n%2
        s.push(remainder)
        n = n//2
    binary_list = map(lambda x: str(x),s.get_stack())
    return "".join(binary_list)[::-1]

print(int_to_binary(242))





