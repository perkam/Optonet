import math
from typing import List


class Node:

    def __init__(self, id: str):
        self.id = id


class Link:

    def __init__(self, id: str, first_node: Node, second_node: Node):
        self.id = id
        self.first_node = first_node
        self.second_node = second_node
        self.capacity = 92


class Demand:

    def __init__(self, id, first_node: Node, second_node: Node, paths: List[List[Link]], value: int):
        self.id = id
        self.first_node = first_node
        self.second_node = second_node
        self.paths = paths
        self.value = int(float(value))


class Network:

    def __init__(self, nodes: List[Node], links: List[Link], demands: List[Demand]):
        self.nodes = nodes
        self.links = links
        self.demands = demands


class TransponderCard:

    def __init__(self, capacity: int, cost: int):
        self.capacity = capacity
        self.cost = cost

    def necessary_lambdas(self, demand_value):
        return math.ceil(demand_value / self.capacity)
