#functions for graph.py

def find_lowest_cost_node(costs,processed):
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node,cost in costs.items():
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node