class node:

	def __init__(self):
		self.label = "empty"
		self.degree = 0
		self.root = False

	def setLabel(self, name):
		self.label = name

	def setDegree(self,num):
		self.degree = num

	def setRoot(self,isRoot):
		self.root = isRoot



class edge:
	
	def __init__(self):
		self.start = "" 
		self.end = ""
		self.weight = 0
		
	def setStart(self,sNode):
		self.start = sNode

	def setEnd(self,eNode):
		self.end = eNode
		
	def setWeight(self,val):
		self.weight = val

class graph:
	
	def __init__(self):
		self.edges = []
		self.vertices = []
		self.label = "empty"

	def setLabel(self,name):
		self.label = name

	def addEdge(self,edge):
		self.edges.append(edge)

	def addVertex(self,node):
		self.vertices.append(node)


	def dumpGraph(self):
		for e in self.edges:
			print e.start, e.end, e.weight
		for v in self.vertices:
			print v.label, v.degree, v.root
		print self.label
