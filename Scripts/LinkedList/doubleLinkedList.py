# implementation of doubly linked list

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

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
                print(current_node.value, end= ' ')
                current_node = current_node.next
    
    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
            print(self.tail)

newLinkedList = LinkedList()
newLinkedList.append(5)
newLinkedList.append(10)
newLinkedList.append(15)
print(newLinkedList)
newLinkedList.print_list()






