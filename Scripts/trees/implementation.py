class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        newNode = Node(data)
        if not self.root:
            self.root = newNode
            return
        else:
            currentNode = self.root
            while True:
                if newNode.data < currentNode.data:
                    if currentNode.left:
                       currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                        return
                else:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode
                        return

myTree = Tree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(6)
myTree.insert(1)
myTree.insert(15)
myTree.insert(170)