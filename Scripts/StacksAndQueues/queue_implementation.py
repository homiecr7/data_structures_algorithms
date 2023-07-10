class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def peak(self):
        print(f"First Member: {self.first.data}")

    def enqueue(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
            self.length += 1
        else:
            self.last.next = newNode
            self.last = newNode
            self.length += 1

    def dequeue(self):
        if self.length == 1:
            print(f"This is the last memeber: {self.first.data}")
            self.first = None
            self.last = None
            self.length -= 1
            print("Queue is empty")
        else:
            print(f"Item dequeued: {self.first.data}")
            self.first = self.first.next
            self.length -= 1
    
    def isEmpty(self):
        if self.length == 0:
            print(True)
        else:
            print(False)

myQueue = Queue()
# myQueue.enqueue("Google")
myQueue.isEmpty()
# myQueue.enqueue("Discord")
# myQueue.enqueue("Udemy")
# myQueue.dequeue()
# myQueue.dequeue()
# myQueue.dequeue()
