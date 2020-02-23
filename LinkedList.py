class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_list(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def len_of_list(self):

        if not self.head:
            print("List is empty")
        curr_node = self.head
        length = 0

        while curr_node:
            length += 1
            curr_node  = curr_node.next
        return length



    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_value(self,value,data):
        new_node = Node(data)
        current_node = self.head
        value_found = False

        if not current_node:
            print("List is empty. The given value is the first node")
            self.head = new_node

        while current_node:
            if current_node.data == value:
                new_node.next = current_node.next
                current_node.next = new_node
                value_found = True
            current_node = current_node.next
            if not current_node and not value_found:
                print("{} is not in the list".format(value))
    def insert_after_node(self,prev_node,data):

        if not prev_node:
            print("Previous not is not present. If you are looking to make {} the head node, use prepend".format(data))
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def delete_node_with_value(self,value):

        value_present = False
        curr_node = self.head

        if not curr_node:
            print('The list is empty')
            return

        if curr_node.data == value:
            self.head = curr_node.next
            curr_node.next = None
            return

        prev_node = curr_node
        curr_node = curr_node.next

        while curr_node:

            if curr_node.data == value:
                prev_node.next = curr_node.next
                curr_node.next = None

                value_present = True

            prev_node = curr_node
            curr_node = curr_node.next

        if not value_present and self.head:
            print("Value is not found in the list")

    def swap_nodes(self, value1, value2):

        curr_node = self.head



llist = Linkedlist()
llist.append(1)
llist.append(2)
llist.prepend(3)
llist.insert_after_value(1,99)
llist.insert_after_node(llist.head,100)
llist.print_list()
print("\n")
llist.delete_node_with_value(3)
llist.print_list()
print("\n")
print(llist.len_of_list())


