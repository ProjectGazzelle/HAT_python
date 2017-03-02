import sys
import myGraph
import re

print sys.argv[1]
filename = sys.argv[1]
HAT_file = open(filename,'r')

HAT_graph = myGraph.graph()


def setGraphLabel(graph,newLabel):
	graph.setLabel(newLabel)
	
def genNode(graph,parameters):
	newNode = myGraph.node()
	newNode.setLabel(parameters[0])
	newNode.setDegree(int(parameters[1]))
	if parameters[2]:
		newNode.setRoot(True)
	else:
		newNode.setRoot(False)
	graph.addVertex(newNode)

def genEdge(graph,parameters):
	newEdge = myGraph.edge()
	newEdge.setStart(parameters[0])
	newEdge.setEnd(parameters[1])
	newEdge.setWeight(int(parameters[2]))
	graph.addEdge(newEdge)


def parseGraph(inFile,graph):
	for line in inFile:
		words = re.split(' ',line)
	if words[0] == '#' or words[0][0] == '#':
		pass
	if words[0] == "label:":
		graph.setLabel(words[1])
	if words[0] == "node:":
		genNode(graph,words[1:])
	if words[0] == "edge:":
		genEdge(graph,words[1:])



parseGraph(HAT_file,HAT_graph)

HAT_graph.dumpGraph()
