import sys
import myGraph
import re
class HATParser:
	def __init__(self):
		self.name = "HATParser"
	
	def genNode(self,graph,parameters):
		#Method to create a new node object and and add it to the graph
		newNode = myGraph.node()
		newNode.setLabel(parameters[0])
		newNode.setInDegree(int(parameters[1]))
		newNode.setOutDegree(int(parameters[2]))
		if parameters[3]:
			newNode.setRoot(True)
		else:
			newNode.setRoot(False)
		graph.addVertex(newNode)

	def genEdge(self,graph,parameters):
		#Method to create a new edge object and add it to the graph
		newEdge = myGraph.edge()
		newEdge.setStart(parameters[0])
		newEdge.setEnd(parameters[1])
		newEdge.setWeight(int(parameters[2]))
		graph.addEdge(newEdge)


	def parseGraph(self,inFile,graph):
		#Method to parse a .hat file and create a graph object from the file
		for line in inFile:
			words = re.split(' ',line)
			if words[0] == '#' or words[0][0] == '#':
				pass
			if words[0] == "label:":
				graph.setLabel(words[1])
			if words[0] == "node:":
				self.genNode(graph,words[1:])
			if words[0] == "edge:":
				self.genEdge(graph,words[1:])

