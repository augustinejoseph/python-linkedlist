class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                # Selecting the previous node from last. The reference of the last node is empty. 
                # So the the reference of previous node to the next node(last node) is empty
                n = n.ref
            n.ref = None

linkdedlist = LinkedList()
linkdedlist.delete_last()