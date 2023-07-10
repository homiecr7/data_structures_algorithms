class myStack():
    def __init__(self):
        self.data = {}
        self.length = 0
    
    def __str__(self):
        return str(self.__dict__)
    
    def push(self, value):
        self.data[self.length] = value
        self.length += 1
    
    def peak(self):
        print(self.data[self.length - 1])
    
    def pop(self):
        if self.length == 1:
            print(f"This is last plate in stack: {self.data[self.length - 1]}")
            del self.data
        else:
            print(f"poped item: {self.data[self.length - 1]}")
            del self.data[self.length - 1]
            self.length -= 1

mystack = myStack()
mystack.push(5)
mystack.push(8)
mystack.push(9)
mystack.peak()
mystack.pop()
mystack.peak()
mystack.pop()
mystack.pop()

