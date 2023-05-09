# Add element when linked list is empty

class Node():
    def __init__(self, data):
        self.ref = None
        self.data = data

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_empty(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("Linked list is not empty")

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n = n.ref


linkedList = LinkedList()
linkedList.insert_empty(10)
linkedList.print_list()
