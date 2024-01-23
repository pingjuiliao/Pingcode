#!/usr/bin/env python3

import heapq
import random

from pingcode.util import Problem


class KBestPairFromTwoList(Problem):
    def kbest_naive(self, k, nums0, nums1):
        pairs = []
        for x in nums0:
            for y in nums1:
                pairs.append((x + y, y, (x, y)))
        return [pair for _, _, pair in sorted(pairs)[:k]]

    def kbest_qselect(self, k, nums0, nums1):
        pairs = []
        for x in nums0:
            for y in nums1:
                pairs.append((x + y, y, (x, y)))
        kbest = self.qselect(k, pairs)
        return [pair for _, _, pair in kbest]

    def qselect(self, k, pair_list):
        if len(pair_list) <= k:
            return pair_list

        idx = random.randint(0, len(pair_list) - 1)
        pivot = pair_list[idx]

        left = [pair for pair in pair_list if pair <= pivot]
        print(left)
        if k <= len(left):
            return self.qselect(k, left)

        right = [pair for pair in pair_list if pair > pivot]
        return left + self.qselect(k - len(left), right)

    def kbest_dijkstra(self, k, nums0, nums1):
        nums0 = sorted(nums0)
        nums1 = sorted(nums1)

        pq = [((nums0[0] + nums1[0], nums1[0]), 0, 0)]
        visited = set()
        kbest = []

        while pq:
            _, i, j = heapq.heappop(pq)
            kbest.append((nums0[i], nums1[j]))
            if len(kbest) == k:
                break

            if i + 1 < len(nums0) and (i + 1, j) not in visited:
                heapq.heappush(pq,
                               ((nums0[i + 1] + nums1[j], nums1[j]),
                                 i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums1) and (i, j + 1) not in visited:
                heapq.heappush(pq,
                               ((nums0[i] + nums1[j + 1], nums1[j + 1]),
                                i, j + 1))
                visited.add((i, j + 1))

        return kbest



    def import_testcases(self):
        a, b = [4, 1, 5, 3], [2, 6, 3, 4]
        test_out = [(1, 2), (1, 3), (3, 2), (1, 4)]
        self.add_testcase((len(a), a, b), test_out)
        a = [24, 3, 73, 72, 52, 54, 74, 94, 10, 97, 68, 61, 79, 44, 44,
             26, 49, 15, 73, 61, 31, 43, 48, 92, 1, 30, 87, 19, 33, 83,
             9, 81, 96, 23, 69, 37, 20, 31, 43, 61, 76, 62, 88, 77, 69,
             87, 7, 28, 91, 34, 14, 37, 23, 72, 88, 86, 90, 31, 9, 31,
             25, 93, 28, 36, 18, 98, 46, 6, 62, 57, 89, 21, 43, 94, 41,
             15, 2, 13, 54, 15, 25, 72, 100, 95, 54, 55, 69, 43, 49, 92,
             59, 56, 84, 42, 94, 85, 6, 18, 16, 88]
        b = [100, 81, 54, 78, 98, 94, 27, 15, 87, 55, 24, 49, 54, 5, 37,
             97, 51, 15, 64, 49, 77, 72, 66, 98, 58, 5, 94, 2, 4, 8, 4,
             41, 97, 27, 54, 57, 57, 76, 16, 83, 66, 95, 7, 35, 73, 19,
             87, 71, 1, 77, 27, 76, 86, 71, 50, 18, 91, 100, 93, 26, 37,
             56, 68, 38, 63, 46, 50, 48, 68, 99, 30, 68, 99, 5, 54, 73,
             85, 46, 99, 16, 62, 68, 80, 71, 62, 56, 76, 56, 80, 67, 92,
             65, 81, 34, 58, 43, 72, 13, 63, 78]
        test_out = [(1, 1), (2, 1), (1, 2), (3, 1), (2, 2), (3, 2),
                    (1, 4), (1, 4), (2, 4), (2, 4), (1, 5), (1, 5),
                    (1, 5), (6, 1), (6, 1), (3, 4), (3, 4), (2, 5),
                    (2, 5), (2, 5), (7, 1), (6, 2), (6, 2), (3, 5),
                    (3, 5), (3, 5), (1, 7), (7, 2), (2, 7), (1, 8),
                    (9, 1), (9, 1), (6, 4), (6, 4), (6, 4), (6, 4),
                    (3, 7), (2, 8), (10, 1), (9, 2), (9, 2), (7, 4),
                    (7, 4), (6, 5), (6, 5), (6, 5), (6, 5), (6, 5),
                    (6, 5), (3, 8), (10, 2), (7, 5), (7, 5), (7, 5),
                    (9, 4), (9, 4), (9, 4), (9, 4), (6, 7), (6, 7),
                    (13, 1), (10, 4), (10, 4), (9, 5), (9, 5), (9, 5),
                    (9, 5), (9, 5), (9, 5), (7, 7), (6, 8), (6, 8),
                    (1, 13), (14, 1), (13, 2), (10, 5), (10, 5), (10, 5),
                    (7, 8), (2, 13), (15, 1), (15, 1), (15, 1), (14, 2),
                    (9, 7), (9, 7), (3, 13), (1, 15), (1, 15), (16, 1),
                    (15, 2), (15, 2), (15, 2), (13, 4), (13, 4), (10, 7),
                    (9, 8), (9, 8), (2, 15), (2, 15)]
        self.add_testcase((len(a), a, b), test_out)

    def solve(self, test_in):
        k, num_list0, num_list1 = test_in
        result = self.kbest_dijkstra(k, num_list0, num_list1)
        return sorted(result, key=lambda x: (x[0]+x[1], x[1]))
