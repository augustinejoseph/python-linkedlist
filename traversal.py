# List of operations:
# Add
# Remove
# Traverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class linkedlist contains head, which is the first linkedlist
# Initailly head and linkedlist will be empty

class linkedList():
    def __init__(self):
        self.head = None
    
    def printList(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

# To show the empty list.
LL1 = linkedList()
LL1.printList()