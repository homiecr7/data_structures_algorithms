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
                    
    def lookup(self, value):
        if not self.root:
            print("No tree found")
        else:
            currentNode = self.root
            while currentNode:
                if currentNode.data > value:
                    currentNode = currentNode.left
                elif currentNode.data < value:
                    currentNode = currentNode.right
                elif currentNode.data == value:
                    print("Found")
                    return
            print("Not Found")
    
    def breadthFirstSearch(self):
        currentNode = self.root
        visited = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            visited.append(currentNode.data)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return visited
    
    def breadthFirstSearchR(self, visited, queue):
        if not queue:
            return visited
        currentNode = queue.pop(0)
        visited.append(currentNode.data)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        return self.breadthFirstSearchR(visited, queue)
        

myTree = Tree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(8)
myTree.insert(10)
myTree.insert(120)
myTree.insert(130)
# myTree.lookup(140)
print(myTree.breadthFirstSearch())
print(myTree.breadthFirstSearchR([], [myTree.root]))

#     9
#  4      20
# 8 10  120 130