
# Linked List Implementation in Python
#### Linkedlist can be useful when:

1. You want to insert items easily in between other items.
2. The size of the total collection is unknown.
3. You don’t need random access when searching for items.
4. There is no concern about memory usage for storing the data.


#### The following code is an implementation of a linked list in Python using classes.

The Node Class
The Node class represents a single node in the linked list. It has two instance variables: data to store the data for the node and next to reference the next node in the list. The __init__ method is used to initialize the values of these variables.

```ruby
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# class linkedlist contains head, which is the first linkedlist
# Initailly head and linkedlist will be empty

class LinkedList():
    def __init__(self):
        self.head = None
```

The code defines a Node class with two attributes: data and ref. The data attribute stores the value of the node, while the ref attribute stores a reference to the next node in the list.

The LinkedList class is then defined, which represents the linked list data structure. It has one attribute: head. Initially, the value of head is set to None, indicating that the linked list is empty.

## Insert Methods
```
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
```
#### add_begin(self, data):
 This method adds a new node to the beginning of the linked list. It creates a new node with the given data value and sets its ref attribute to the current head of the linked list. Then it sets the head attribute of the linked list to the new node.

#### add_end(self, data): 
This method adds a new node to the end of the linked list. It first creates a new node with the given data value. If the linked list is empty (i.e. self.head is None), it sets the head attribute of the linked list to the new node. Otherwise, it traverses the linked list starting from the head node until it reaches the last node (i.e. the node whose ref attribute is None). Then it sets the ref attribute of the last node to the new node.

#### add_before(self, data, x): 
This method adds a new node with the given data value before the node with the given value x. It first checks if the linked list is empty. If it is, it prints a message and returns. If the node with value x is the first node in the linked list, it creates a new node with the given data value and sets its ref attribute to the current head of the linked list. Then it sets the head attribute of the linked list to the new node. Otherwise, it traverses the linked list starting from the head node until it reaches the node whose ref attribute points to the node with value x. It creates a new node with the given data value and sets its ref attribute to the node whose data value is x. Then it sets the ref attribute of the previous node to the new node.

#### insert_empty(self, data): 
This method adds a new node with the given data value to an empty linked list. If the linked list is empty (i.e. self.head is None), it creates a new node with the given data value and sets the head attribute of the linked list to the new node. Otherwise, it prints a message indicating that the linked list is not empty.

## Delete Methods
```
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
```

#### delete_first(self): 
This method deletes the first node from the linked list. If the linked list is empty (i.e. self.head is None), it prints a message indicating that the list is empty. Otherwise, it sets the head attribute of the linked list to the ref attribute of the current head node.

#### delete_last(self): 
This method deletes the last node from the linked list. If the linked list is empty (i.e. self.head is None), it prints a message indicating that the list is empty. Otherwise, it traverses the linked list starting from the head node until it reaches the second-to-last node (i.e. the node whose ref attribute points to the last node). Then it sets the ref attribute of the second-to-last node to None.

#### delete_by_value(self, x): 
This method deletes the node with the given x value from the linked list. If the linked list is empty (i.e. self.head is None), it prints a message indicating that the list is empty and returns. If the node with value x is the first node in the linked list, it sets the head attribute of the linked list to the ref attribute of the current head node. Otherwise, it traverses the linked list starting from the head node until it reaches the node whose ref attribute points to the node with value x. Then it sets the ref attribute of the previous node to the ref attribute of the node with value x. If the node with value x is not found in the linked list, it prints a message indicating that the node is not found and returns.

## Reverse Methods

```
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
```
#### reverse(self): 
This method reverses the linked list in place. If the linked list is empty (i.e. self.head is None), it prints a message indicating that the list is empty and returns. Otherwise, it initializes prev_node to None and current_node to the head node.

Then, it enters a loop that iterates over the nodes in the linked list. At each iteration, it first saves the reference to the next node in the next_node variable. Then, it sets the ref attribute of the current_node to the prev_node, effectively reversing the pointer from the current_node to the prev_node. Next, it updates prev_node to be current_node and current_node to be next_node.

Finally, it sets the head attribute of the linked list to prev_node, which is the last node in the original linked list and the first node in the reversed linked list.

## Display node data:
```
    def printList(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end="")
                n = n.ref
```
#### printList(self): 
This method prints the contents of the linked list in the format "data1 --> data2 --> ... --> dataN" where data1 to dataN are the values stored in the linked list nodes. If the linked list is empty (i.e. self.head is None), it prints a message indicating that the list is empty and returns. Otherwise, it initializes n to self.head, which is the first node in the linked list.

Then, it enters a loop that iterates over the nodes in the linked list. At each iteration, it prints the data attribute of the n node, followed by an arrow (-->), using the print() function. Then, it updates n to be the next node in the linked list (n.ref).

The loop continues until it reaches the end of the linked list, which is indicated by n being None.
