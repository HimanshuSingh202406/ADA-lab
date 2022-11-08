import sys 
class Graph():

	def __init__(self, sides):
		self.V = sides
		self.graph = [[0 for column in range(sides)]
					for row in range(sides)]
	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

	def minimumKey(self, key, mstSet):
		min = sys.maxsize
		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index
	def primMST(self):
		key = [sys.maxsize] * self.V
		parent = [None] * self.V 		
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1 
		for cout in range(self.V):
			u = self.minimumKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):

				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u
		self.printMST(parent)

g = Graph(5)
g.graph = 	[[ 11, 9, 12, 6, 8],
			[ 14, 55, 4, 61, 5 ],
			[9, 12, 0, 8, 7 ],
			[ 16, 52, 0, 9, 11] ,
			[ 8, 5, 14, 11, 16 ]]
g.primMST()
