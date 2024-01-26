#!/usr/bin/env python3

import collections

from pingcode.util import Problem


class GraphNode:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = []


class TravelingSalesman(Problem):

    def build_graph(self, num_nodes, edges, start_node_idx):
        graph = [GraphNode(node_id) for node_id in range(num_nodes + 1)]
        graph[-1].id = 0

        for u, v, distance in edges:
            if u > v:
                u, v = v, u
            graph[u].neighbors.append((graph[v], distance))
            graph[v].neighbors.append((graph[u], distance))
            if u == start_node_idx:
                graph[-1].neighbors.append((graph[v], distance))
                graph[v].neighbors.append((graph[-1], distance))

        return graph

    def tsp_viterbi_frozenset(self, num_nodes, edges, start_node_idx):
        # turn graph into nodes
        graph = self.build_graph(num_nodes, edges, start_node_idx)
        start_node = graph[start_node_idx]
        end_node = graph[-1]

        dp = collections.defaultdict(
            lambda: collections.defaultdict(lambda: float('Inf'))
        )
        dp[frozenset([start_node])][start_node] = 0
        dp_back = collections.defaultdict(
            lambda: collections.defaultdict(lambda: None)
        )

        queue = collections.deque()
        queue.append((frozenset([graph[start_node_idx]]), start_node))

        while queue:
            subset, node = queue.popleft()
            for neighbor_node, distance in node.neighbors:
                if neighbor_node in subset:
                    continue

                new_subset = subset.union(frozenset([neighbor_node]))
                if dp[new_subset][neighbor_node] > dp[subset][node] + distance:
                    dp[new_subset][neighbor_node] = dp[subset][node] + distance
                    dp_back[new_subset][neighbor_node] = node
                    queue.append((new_subset, neighbor_node))

        return (dp[frozenset(graph)][end_node],
                self.backtrack(dp_back, frozenset(graph), end_node))

    def backtrack(self, dp_back, graph_set, curr):
        if curr is None:
            return []
        prev = dp_back[graph_set][curr]
        subset = graph_set - frozenset([curr])
        return self.backtrack(dp_back, subset, prev) + [curr.id]

    def import_testcases(self):
        # graph representations
        graph = (4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2), (1, 3, 6)], 0)
        out = (14, [0, 1, 3, 2, 0])
        self.add_testcase(graph, out)

        graph = (4, [(0, 1, 1), (0, 2, 5), (1, 2, 1), (2, 3, 2),
                     (1, 3, 6), (3, 0, 1)],
        0)
        out = (5, [0, 1, 2, 3, 0])
        self.add_testcase(graph, out)

        graph = (11, [(0,1,29),(0,2,20),(0,3,21),(0,4,16),(0,5,31),(0,6,100),
                      (0,7,12),(0,8,4),(0,9,31),(0,10,18),(1,2,15),(1,3,29),
                      (1,4,28),(1,5,40),(1,6,72),(1,7,21),(1,8,29),(1,9,41),
                      (1,10,12),(2,3,15),(2,4,14),(2,5,25),(2,6,81),(2,7,9),
                      (2,8,23),(2,9,27),(2,10,13),(3,4,4),(3,5,12),(3,6,92),
                      (3,7,12),(3,8,25),(3,9,13),(3,10,25),(4,5,16),(4,6,94),
                      (4,7,9),(4,8,20),(4,9,16),(4,10,22),(5,6,95),(5,7,24),
                      (5,8,36),(5,9,3),(5,10,37),(6,7,90),(6,8,101),(6,9,99),
                      (6,10,84),(7,8,15),(7,9,25),(7,10,13),(8,9,35),(8,10,18),
                      (9,10,38)],
        0)
        out = (253, [0, 7, 4, 3, 9, 5, 2, 6, 1, 10, 8, 0])
        self.add_testcase(graph, out)

        graph = (16, [(1, 2, 0), (11, 5, 5), (9, 8, 4), (6, 1, 4), (5, 13, 5),
                      (12, 11, 4), (14, 8, 0), (0, 11, 3), (10, 12, 3),
                      (5, 5, 1), (7, 0, 1), (10, 5, 1), (11, 5, 3), (13, 11, 4),
                      (11, 11, 3), (5, 12, 5), (14, 7, 3), (8, 15, 4),
                      (11, 14, 3), (11, 14, 3), (7, 10, 5), (5, 8, 3),
                      (9, 9, 5), (13, 9, 5), (6, 15, 4), (11, 2, 2), (0, 6, 5),
                      (3, 1, 4), (1, 8, 4), (7, 3, 4), (4, 8, 1), (6, 1, 3),
                      (1, 1, 2), (11, 5, 1), (0, 2, 0), (2, 0, 0), (0, 11, 2),
                      (4, 5, 5), (5, 0, 3), (1, 7, 1), (1, 0, 2), (3, 9, 2),
                      (15, 0, 2), (14, 1, 2), (12, 4, 3), (7, 2, 5), (10, 3, 0),
                      (14, 4, 4), (12, 15, 4), (10, 4, 2), (8, 8, 4),
                      (13, 0, 5), (4, 1, 2), (1, 4, 1), (5, 3, 3), (7, 1, 1),
                      (7, 14, 0), (8, 2, 4), (7, 11, 2), (13, 8, 4), (0, 4, 0),
                      (12, 13, 1), (3, 2, 1), (3, 3, 0), (5, 7, 0), (6, 0, 4),
                      (14, 14, 2), (12, 6, 5), (6, 13, 3), (0, 1, 3), (5, 3, 5),
                      (15, 11, 0), (3, 11, 2), (11, 9, 0), (13, 3, 0),
                      (9, 6, 5), (0, 14, 0), (13, 15, 3), (6, 2, 0), (9, 0, 2),
                      (9, 2, 1), (15, 6, 0), (11, 12, 5), (14, 4, 2),
                      (12, 3, 2), (3, 3, 0), (10, 12, 1), (3, 0, 4), (15, 1, 5),
                      (15, 9, 2), (14, 4, 2), (8, 15, 4), (15, 13, 3),
                      (9, 12, 1), (5, 15, 4), (8, 13, 5), (2, 3, 0), (11, 5, 4),
                      (4, 13, 0), (2, 1, 1)],
        0)
        out = (6, [0, 1, 2, 6, 15, 11, 9, 12, 13, 3, 10, 5, 7, 14, 8, 4, 0])
        self.add_testcase(graph, out)

    def solve(self, test_in):
        num_nodes, edges, start_node_idx = test_in
        return self.tsp_viterbi_frozenset(num_nodes,
                                          edges,
                                          start_node_idx)
