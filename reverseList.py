class Node():
    def __init__(self, head):
        self.head = None
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None

    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.ref
            current_node.ref = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

linkedList = LinkedList()
linkedList.reverse()