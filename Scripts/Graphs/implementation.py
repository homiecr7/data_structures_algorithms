class Graph():
    def __init__(self):
        self.numberOfNodes = 0
        self.adjecentList = {}
    
    def addVertex(self, node):
        if node not in self.adjecentList:
            self.adjecentList[node] = []
            self.numberOfNodes += 1
        
    def addEdge(self, node1, node2):
        if (node1 and node2) not in self.adjecentList.keys():
            print("Node doesn't exist")
            return
        else:
            self.adjecentList[node1].append(node2)
            self.adjecentList[node2].append(node1)
            print("Connections added")
            return

    def show_connections(self):
        for node in self.adjecentList:
            print(f'{node} -->> {" ".join(map(str, self.adjecentList[node]))}')

my_graph = Graph()
my_graph.addVertex(1)
my_graph.addVertex(2)
my_graph.addVertex(3)
my_graph.addEdge(1,2)
my_graph.addEdge(1,3)
my_graph.addEdge(2,3)
my_graph.show_connections()