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
    def __str__(self): # print the attributes of the object in the form of dictionary
        return str(self.__dict__)

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
    
    def prepend(self, value):
        newNode = Node(value)
        if self.head == None:
            print("No linked list is present")
            return
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return
    
    def insert(self, position, value):
        newNode = Node(value)
        if position >= self.length:
            print("Since insertion is in last running append function")
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
            return
        elif position == 0:
            if self.head == None:
                print("No linked list is present")
                return
            else:
                newNode.next = self.head
                self.head = newNode
                self.length += 1
                return
        else:
            for i in range(self.length):
                print(i)

myLinkedList = LinkedList()
myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.append(8)
myLinkedList.prepend(2)
myLinkedList.prepend(7)
myLinkedList.insert(2, 9)
myLinkedList.print_list()
