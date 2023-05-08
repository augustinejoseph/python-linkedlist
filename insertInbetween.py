# Adding before first node
# Adding on all other posistions
class Node():
    def __init__(self, data):
        self.data = data
        self.head = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_before(self, data, x):
        # if there is no elements or nodes in the list
        if self.head is None:
            print("List is empty")
            return
        # if the node is added as the first element
        if self.head.data == x:
            newNode = Node(data)
            newNode.head = self.head
            self.head = newNode
            return
        n = self.head
        while n.ref is not None:
            # if the data in the next node is x. Currently at the previous node
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode

linkedList = LinkedList()
linkedList.add_before(10,2)
linkedList.print_list()