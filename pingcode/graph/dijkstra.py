#!/usr/bin/env python3

import heapq

from pingcode.util import Problem


class GraphNode:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = []

class ShortestPath(Problem):
    def build_graph(self, num_nodes, edges):
        graph = [GraphNode(i) for i in range(num_nodes)]
        for u, v, weight in edges:
            graph[u].neighbors.append((v, weight))
            graph[v].neighbors.append((u, weight))
        return graph

    def dijkstra_heap_based(self, graph, start_node, end_node):
        """
        O(E*log(E)) method
        """
        shortest = [float('Inf') for _ in range(len(graph))]
        back = [None for _ in range(len(graph))]

        pq = [start_node]
        while pq:
            node = heapq.heappop(pq)
            for neighbor_node, weight in node.neighbors:


    def import_testcases(self):
        test_in = (4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)])
        test_out = (4, [0, 1, 2, 3])
        self.add_testcase(test_in, test_out)

        test_in2 = (8, [(0, 4, 2), (0, 1, 7), (0, 7, 12), (1, 2, 1), (1, 3, 1),
                        (1, 7, 5), (2, 3, 3), (2, 4, 1), (2, 5, 1), (2, 7, 10),
                        (3, 6, 2), (3, 4, 5), (3, 7, 1)])
        test_out2 = (6, [0, 4, 2, 1, 3, 7])
        self.add_testcase(test_in2, test_out2)

    def solve(self, test_in):
        graph = self.build_graph(test_in[0], test_in[1])
        return self.dijkstra_heap_based(graph, graph[0], graph[-1])


    # def dijkstra_heapdict_based(self):
