graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

def get_lowest_cost_node(costs):
    lowest_cost = 0
    lowest_cost_node = {}
    for node in costs:
        if costs[node] < lowest_cost:
            lowest_cost = costs[node]
            lowest_cost_node = node 