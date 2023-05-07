# Linked List Implementation in Python
#### Linkedlist can be useful when:

1. You want to insert items easily in between other items.
2. The size of the total collection is unknown.
3. You don’t need random access when searching for items.
4. There is no concern about memory usage for storing the data.


#### The following code is an implementation of a linked list in Python using classes.

The Node Class
The Node class represents a single node in the linked list. It has two instance variables: data to store the data for the node and next to reference the next node in the list. The __init__ method is used to initialize the values of these variables.

### The LinkedList Class
The LinkedList class represents the entire linked list. It has one instance variable: head to reference the head node of the list. The __init__ method initializes the head node to None when the list is first created.

### The insert Method
The insert method is used to insert a new node at the end of the linked list. If the list is empty, the new node becomes the head node. Otherwise, the method traverses the list to find the last node and then adds the new node to its next reference.

### The printList Method
The printList method is used to print the data of all the nodes in the linked list. It traverses the list from the head node and prints the data of each node.

### Example
The code creates a linked list with three nodes - "John", "Ben", and "Doe". The first node "John" is created as an instance of the Node class, and the linked list is created as an instance of the LinkedList class. The first node is inserted into the linked list using the insert method. Similarly, the other two nodes are also inserted. Finally, the printList method is called to print the data of all the nodes in the linked list.
