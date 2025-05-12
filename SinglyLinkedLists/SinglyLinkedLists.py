# Define the Node class
class Node:
    # Constructor to initialize the node with data
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    # Constructor initializes the list with an empty head
    def __init__(self):
        self.head = None

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        # Create a new node
        new_node = Node(data)
        # If the list is empty, make new_node the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        # Link the last node to the new node
        current_node.next = new_node

    # Insert a new node at the start of the list
    def insert_at_start(self, data):
        # Create a new node
        new_node = Node(data)
        # If the list is empty, set new_node as head
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert a new node at a specific index
    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return

        position = 0
        current_node = self.head

        # Go to the node just before the target index
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("\nIndex not present")

    # Search for a value in the list
    def search(self, value):
        current_node = self.head
        found = False

        # Go through list until the value is found or list ends
        while current_node:
            if value == current_node.data:
                print(f"\nNode Found -> Data: {current_node.data} | Next: {current_node.next}")
                found = True
                break
            current_node = current_node.next

        if not found:
            print("\nValue Not Found In Linked List")

    # Display all nodes in the list
    def display(self):
        current_node = self.head
        while current_node:
            print(f"Data: {current_node.data} | Next: {current_node.next}")
            current_node = current_node.next

# Create a LinkedList object
myfirstLinkedList = LinkedList()

# Insert values into the LinkedList
myfirstLinkedList.insert_at_end(1)
myfirstLinkedList.insert_at_start(2)
myfirstLinkedList.insert_at_end(3)
myfirstLinkedList.insert_at_end(4)
myfirstLinkedList.insert_at_index(3, 5)

# Display the full linked list
myfirstLinkedList.display()

# Checks for a value in the linked list
myfirstLinkedList.search(2)
