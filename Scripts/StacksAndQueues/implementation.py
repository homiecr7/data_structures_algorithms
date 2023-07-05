class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
            self.length += 1
        else:
            self.top.next = newNode
            self.top = newNode
            self.length += 1
    
    def pop(self):
        if self.length == 1:
            tempNode = self.bottom
            self.bottom = None
            self.top = None
            self.length -= 1
            print(f"This is the last plate in the stack with value: {tempNode.data}")

        elif self.length == 0:
            print("stack is empty")

        else:
            length = 0
            currentNode = self.bottom
            while length != self.length - 2:
                currentNode = currentNode.next
                length += 1
            tempNode = self.top
            print(f"poped data: {tempNode.data}")
            del tempNode
            currentNode.next = None
            self.top = currentNode
            self.length -= 1
             
    def peak(self):
        print(self.top.data)

    def isEmpty(self):
        if self.length == 0:
            print(True)
        else:
            print(False)
        

newStack = Stack()
newStack.push('google')
newStack.push('udemy')
newStack.push('discord')
newStack.peak()
newStack.pop()
newStack.peak()
newStack.pop()
newStack.peak()
newStack.pop()


