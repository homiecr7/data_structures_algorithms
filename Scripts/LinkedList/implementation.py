# creating a linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

myLinkedList = LinkedList()
myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.append(8)
myLinkedList.print_list()
