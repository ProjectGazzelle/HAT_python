

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
