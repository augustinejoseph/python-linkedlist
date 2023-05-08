class Node():
    def __init__(self, data):
        self.data = data
        self.head = None
    

class LinkedList():
    def __init__(self):
        self.head = None
    
    def add_begin(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n= n.ref

linkedList = LinkedList()
linkedList.add_begin("John")
linkedList.add_begin("Mathew")
linkedList.print_list()