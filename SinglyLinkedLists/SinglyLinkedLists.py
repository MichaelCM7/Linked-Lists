#Create the class Node
class Node:
    #Create the method
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def insert_at_start(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self,index,data):
        if index == 0:
            self.insert_at_start(data)
            return

        position = 0
        current_node = self.head
        while current_node != None and position+1 != index:
            position += 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("\nIndex not present")

    def search(self, value):
        current_node = self.head
        found = False
        while current_node:
            if value == current_node.data:
                print(f"\nNode Found -> Data: {current_node.data} | Next: {current_node.next}")
                found = True
                break
            current_node = current_node.next
        if not found:
            print("\nValue Not Found In Linked List")

    def display(self):
        current_node = self.head
        while current_node:
            print(f"Data: {current_node.data} | Next: {current_node.next}")
            current_node = current_node.next

myfirstLinkedList = LinkedList()

myfirstLinkedList.insert_at_end(1)
myfirstLinkedList.insert_at_start(2)
myfirstLinkedList.insert_at_end(3)
myfirstLinkedList.insert_at_end(4)
myfirstLinkedList.insert_at_index(3,5)

myfirstLinkedList.display()

myfirstLinkedList.search(2)