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
            while current_node != None:
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
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
            return
    
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
            current_node = self.head
            for i in range(self.length):
                if i == position - 1:
                    newNode.next = current_node.next
                    current_node.next = newNode
                    self.length += 1
                else:
                    current_node = current_node.next
    def remove(self, index):
        currentNode = self.head
        counter = 0
        while counter != index - 1:
            currentNode = currentNode.next
            counter += 1
        deletedNode = currentNode.next
        currentNode.next = deletedNode.next
        del deletedNode
        self.length -= 1
        return
    
    def reverse(self):
        if self.length <= 0 or self.length == 1:
            print("not linked list present or only one node present")
        else:
            currentNode = self.head
            nextNode = None
            previousNode = None

            while currentNode != None:
                nextNode = currentNode.next
                currentNode.next = previousNode
                previousNode = currentNode
                currentNode = nextNode
            tempNode = self.head
            self.head = self.tail
            self.tail = tempNode
            return

myLinkedList = LinkedList()
myLinkedList.append(1)
myLinkedList.append(2)
myLinkedList.prepend(2)
myLinkedList.prepend(7)
myLinkedList.insert(2, 9)
myLinkedList.print_list()
myLinkedList.insert(28, 19)
myLinkedList.print_list()
# myLinkedList.print_list()
# myLinkedList.remove(3)
# myLinkedList.remove(1)
# myLinkedList.print_list()
myLinkedList.reverse()
myLinkedList.print_list()


