from collections import deque
from functions import *

class graph:

	def __init__(self, wheighted=True):
		self.dict = dict()
		self.number_of_nodes = 0
		self.wheighted = wheighted

	def __str__(self):
		s = "Graph including {} nodes.\n".format(self.number_of_nodes)
		for node in self.dict.keys():
			s += node+"\n"
		return s


	def __setitem__(self, node, edges):
		if type(edges) != list:
			edges = [edges]

		for edge in edges:
			if self.wheighted:
				ending_node, weight = edge
				if ending_node not in self.dict.keys():
					self.dict[ending_node] = {}
					self.number_of_nodes += 1

				if node in self.dict.keys():
					self.dict[node][ending_node] = weight
				else:
					self.dict[node] = {ending_node : weight}
					self.number_of_nodes += 1
			else:
				ending_node = edges
				if ending_node not in self.dict.keys():
					self.dict[ending_node] = []
					self.number_of_nodes += 1

				if node in self.dict.keys():
					self.dict[node].append(ending_node)
				else:
					self.dict[node] = [ending_node]
					self.number_of_nodes += 1



	def __getitem__(self,node):
		return self.dict[node]

	def breadth_first(self, starting_node, ending_node):
		if self.wheighted:
			raise TypeError("This graph is a weighted graph. Breadth-first algorithm can't be applied to this graph.")
		else:
			if starting_node == ending_node:
				return [starting_node]
			else:
				queue = deque([(starting_node,a) for a in self.dict[starting_node]])
				searched = []
				test = True
				previous_node = starting_node
				while test and len(queue) != 0:
					previous_node, next_node = queue.popleft()
					if next_node not in searched:
						if next_node == ending_node:
							test = False
						else:
							queue += [(next_node, a) for a in self.dict[next_node]]
							searched.append(next_node)
				if not test:
					path = self.breadth_first(starting_node,previous_node)
					path.append(next_node)
					return path
				else:
					print("There is no such path.")

	def dijkstra(self, starting_node):
		"""Runs the Dijkstra's algorithm on the graph. This method returns the dictionnary of the costs (from the starting node to the other nodes) and the dictionnary of the parents."""
		if not self.wheighted:
			raise TypeError("This graph is not a weighted graph. Dijkstra's algorithm can't be applied to this graph.")
		else:
			#costs disctionnary
			costs = {}
			infty = float("inf")
			for key in self.dict.keys():
				costs[key] = infty
			costs.update(self.dict[starting_node])

			#parents dictionnary
			parents = {}
			for key in self.dict.keys():
				parents[key] = None
			for key,value in self.dict[starting_node].items():
				parents[key] = starting_node

			processed = []
			node = find_lowest_cost_node(costs,processed)
			while node is not None:
				cost = costs[node]
				neighbors = self.dict[node]
				for neighbor in neighbors.keys():
					new_cost = cost + neighbors[neighbor]
					if new_cost < costs[neighbor]:
						costs[neighbor] = new_cost
						parents[neighbor] = node
				processed.append(node)
				node = find_lowest_cost_node(costs,processed)

			return costs, parents



g = graph()
g["start"] = [("A",6),("B",2)]
g["A"] = ("finish",1)
g["B"] = [("A",3),("finish",5)]
costs, parents = g.dijkstra("start")
print(costs)
print(parents)