class Node():
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def delete_by_value(self, x):
        if self.head is None:
            print("List is empty")
        # if the value is at the first posistion 
        if self.head.data == x:
              self.head = self.head.ref
              return
        # Traversing to the previous node
        n = self.head
        while n.ref  is  not None:
            # When the condition is correct, come out of while loop
            if n.ref.data == x :
                break
            n = n.ref
        if n.ref is None:
            print("The node is not found")
        # As the loops comes out of while loop after finding the previous node
        else:
            n.ref = n.ref.ref
             

        

linkedList = LinkedList()
linkedList.delete_by_value()