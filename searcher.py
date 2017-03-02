

class searcher:

	def __init__(self):
		self.name = "Graph Searcher"

	def findWeakestNode(self,vertices):
		weakNode = vertices[0]
		for node in vertices:
			if node.OutDegree > weakNode.outDegree:
				weakNode = node
		return node


	def findLeaves(self,nodes):
		leaves = []
		for n in nodes:
			if n.OutDegree == 0:
				leaves.append(n)
		return leaves

	def findInternal(self,nodes):
		internal = []
		for n in nodes:
			if n.OutDegree != 0:
				internal.append(n)

	def findRoot(self,nodes):
		for n in nodes:
			if n.label == "root":
				return n

	def findRootPath(leaf,edges):
		rootPath = []
		pathCost = 0
		currentNode = leaf
		rootPath.append(leaf)
		while currentNode != "root":
			for e in edges:
				if e.end == currentNode:
					rootPath.append(e.start)
					currentNode = e.start
					pathCost += e.weight
		return pathCost,rootPath 

	def findCheapestPath(self, graph):
		cheapPath = []
		cheapCost = 10000000000
		leaves = self.findLeaves(graph.vertices)
		for leaf in leaves:
			cost,path = self.findRootPath(leaf,graph.edges)
			if cost < cheapCost:
				cheapPath = path
		return cheapPath,cheapCost
