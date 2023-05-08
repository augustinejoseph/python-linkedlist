# If linkedlist is empty, it is the first node and is newly created.
# Last node is identified, if the reference of the node is empty, then it is last
class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode
        
    def printList(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

LL1 = LinkedList()
LL1.add_end(10)
LL1.add_end(9)
LL1.printList()
