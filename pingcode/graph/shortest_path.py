#!/usr/bin/env python3

import collections
import heapq

from pingcode.util import Problem


class GraphNode:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = []

    def __lt__(self, node):
        return self.id < node.id

class ShortestPath(Problem):
    def build_graph(self, num_nodes, edges):
        graph = [GraphNode(i) for i in range(num_nodes)]
        for u, v, weight in edges:
            graph[u].neighbors.append((graph[v], weight))
            graph[v].neighbors.append((graph[u], weight))
        return graph


    def backtrack(self, back, node):
        if node is None:
            return []
        return self.backtrack(back, back[node]) + [node.id]


    def dijkstra_heap_based(self, start_node, end_node):
        """
        O(E*log(E)) method
        """
        # maps that calculates distances
        distances = collections.defaultdict(lambda: float('Inf'))
        back = collections.defaultdict(None)
        visited = set()

        pq = [(0, start_node, None)]
        while pq:
            distance, node, back_node = heapq.heappop(pq)
            if distance < distances[node]:
                distances[node] = distance
                back[node] = back_node
            visited.add(node)

            for neighbor_node, weight in node.neighbors:
                if neighbor_node in visited:
                    continue
                if distances[node] + weight < distances[neighbor_node]:
                    heapq.heappush(pq,
                                   (distances[node] + weight,
                                    neighbor_node,
                                    node))

        if distances[end_node] == float('Inf'):
            return None
        return distances[end_node], self.backtrack(back, end_node)


    def import_testcases(self):
        test_in = (4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)])
        test_out = (4, [0, 1, 2, 3])
        self.add_testcase(test_in, test_out)

        test_in1 = (4, [(0, 1, 1), (2, 3, 1)])
        test_out1 = None
        self.add_testcase(test_in1, test_out1)

        test_in2 = (8, [(0, 4, 2), (0, 1, 7), (0, 7, 12), (1, 2, 1),
                        (1, 3, 1), (1, 7, 5), (2, 3, 3), (2, 4, 1),
                        (2, 5, 1), (2, 7, 10), (3, 6, 2), (3, 4, 5),
                        (3, 7, 1)])
        test_out2 = (6, [0, 4, 2, 1, 3, 7])
        self.add_testcase(test_in2, test_out2)


    def solve(self, test_in):
        graph = self.build_graph(test_in[0], test_in[1])
        return self.dijkstra_heap_based(graph[0], graph[-1])


    # def dijkstra_heapdict_based(self):
