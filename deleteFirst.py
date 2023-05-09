class Node():
    def __init__(self, data):
        self.ref = None
        self.data = data
    
class LinkedList():
    def __init__(self):
        self.head = None

    def delete_first(self):
        if self.head is None:
            print('The list is empty')
        else:
             self.head = self.head.ref

linkdedlist = LinkedList()
linkdedlist.delete_first()
