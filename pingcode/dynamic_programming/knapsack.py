#!/usr/bin/env python3

from pingcode.util import Problem


class KnapsackUnboundedProduct(Problem):
    def knapsack(self, capacity, products):
        max_values = [0 for _ in range(capacity + 1)]
        back = [None for _ in range(capacity + 1)]
        for n in range(1, capacity + 1):
            for product_id, product in enumerate(products):
                weight, value = product
                if weight > n:
                    continue
                if max_values[n] < max_values[n - weight] + value:
                    max_values[n] = max_values[n - weight] + value
                    back[n] = product_id

        pick_list = [0 for _ in range(len(products))]
        curr = capacity
        while curr > 0:
            pick = back[curr]
            pick_list[pick] += 1
            weight, value = products[pick]
            curr -= weight

        return max_values[capacity], pick_list

    def knapsack_optimized(self, capacity, products):
        max_values = [0 for _ in range(capacity + 1)]
        back = [None for _ in range(capacity + 1)]
        for product_id, product in enumerate(products):
            weight, value = product
            for n in range(weight, capacity + 1):
                if max_values[n] < max_values[n - weight] + value:
                    max_values[n] = max_values[n - weight] + value
                    back[n] = product_id

        pick_list = [0 for _ in range(len(products))]
        curr = capacity
        while curr > 0:
            pick = back[curr]
            pick_list[pick] += 1
            weight, value = products[pick]
            curr -= weight

        return max_values[capacity], pick_list

    def import_testcases(self):
        test_in = (3, [(1, 2), (2, 5)])
        test_out = (7, [1, 1])
        self.add_testcase(test_in, test_out)

        test_in = (58, [(5, 9), (9, 18), (6, 12)])
        test_out = (114, [2, 4, 2])
        self.add_testcase(test_in, test_out)

        test_in = (92, [(8, 9), (9, 10), (10, 12), (5, 6)])
        test_out = (109, [1, 1, 7, 1])
        self.add_testcase(test_in, test_out)

    def solve(self, test_in):
        capacity, store = test_in
        return self.knapsack_optimized(capacity, store)


class KnapsackBoundedProduct(Problem):
    def knapsack(self, capacity, products):
        max_values = [[0 for _ in range(capacity + 1)]
                      for _ in range(len(products))]
        back = [[0 for _ in range(capacity + 1)] for _ in range(len(products))]
        for product_id, product in enumerate(products):
            weight, value, num_storage = product
            for n in range(weight, capacity + 1):

                # default: as if the new product is not introduced
                max_values[product_id][n] = max_values[product_id - 1][n]
                # back[prodict_id][n] = 0

                for i in range(1, num_storage + 1):
                    if weight * i > n:
                        break
                    new_value = (max_values[product_id - 1][n - weight * i]
                                 + value * i)
                    if max_values[product_id][n] < new_value:
                        max_values[product_id][n] = new_value
                        back[product_id][n] = i

        pick_list = [0 for _ in range(len(products))]
        n = capacity
        for product_id in range(len(products) - 1, -1, -1):
            pick_list[product_id] += back[product_id][n]
            n = n - back[product_id][n] * products[product_id][0]

        return max_values[len(products) - 1][capacity], pick_list

    def import_testcases(self):
        test_in = (3, [(2, 4, 2), (3, 5, 3)])
        test_out = (5, [0, 1])
        self.add_testcase(test_in, test_out)

        test_in = (20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
        test_out = (130, [6, 4, 1])
        self.add_testcase(test_in, test_out)

        test_in = (92, [(1, 6, 6), (6, 15, 7), (8, 9, 8),
                        (2, 4, 7), (2, 20, 2)])
        test_out = (236, [6, 7, 3, 7, 2])
        self.add_testcase(test_in, test_out)

        # if there's a tie between prodcuts, lower product_id comes first
        test_in = (3, [(1, 5, 1), (1, 5, 3)])
        test_out = (15, [1, 2])
        self.add_testcase(test_in, test_out)

        test_in = (3, [(1, 5, 2), (1, 5, 3)])
        test_out = (15, [2, 1])
        self.add_testcase(test_in, test_out)

    def solve(self, test_in):
        capacity, store = test_in
        return self.knapsack(capacity, store)
