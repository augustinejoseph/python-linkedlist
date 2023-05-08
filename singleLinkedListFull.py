# List of operations:
# Add
# Remove
# Traverse

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# class linkedlist contains head, which is the first linkedlist
# Initailly head and linkedlist will be empty

class LinkedList():
    def __init__(self):
        self.head = None
    
    def add_begin(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode
    
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

    def printList(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

# To show the empty list.
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(11)
LL1.add_begin(9)
LL1.add_before(100, 10)
LL1.add_before(90, 10)
LL1.printList()