# List of operations:
# Add
# Remove
# Traverse
# Reverse

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
        
    def insert_empty(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
        else:
            print("Linked list is not empty")

    # Delete Operations
    def delete_first(self):
        if self.head is None:
            print('The list is empty')
        else:
             self.head = self.head.ref
    
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
    
    def delete_by_value(self, x):
        if self.head is None:
            print("List is empty")
            return
        # if the value is at the first posistion 
        if self.head.data == x:
              self.head = self.head.ref
              return
        # Traversing to the previous node
        n = self.head
        while n.ref is  not None:
            # When the condition is correct, come out of while loop
            if x == n.ref.data :
                break
            n = n.ref
        if n.ref is None:
            print("The node is not found")
            return
        # As the loops comes out of while loop after finding the previous node
        else:
            n.ref = n.ref.ref
    
    # Reverse the list
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
    
    # Print
    def printList(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.ref

# To show the empty list.
LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_end(11)
LL1.add_begin(9)
LL1.add_before(100, 10)
LL1.add_before(90, 10)
LL1.delete_first()
LL1.delete_last()
LL1.delete_by_value(900)
LL1.reverse()
LL1.printList()