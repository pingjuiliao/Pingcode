#!/usr/bin/env python3

import random
from pingcode.util import Problem


class QuickSort(Problem):
    def quicksort(self, nums):
        if not nums:
            return []

        rand_idx = random.randint(0, len(nums) - 1)
        pivot = nums[rand_idx]

        left, mid, right = [], 0, []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n == pivot:
                mid += 1
            else:
                right.append(n)

        left = self.quicksort(left)
        right = self.quicksort(right)
        return left + [pivot] * mid + right

    def import_testcases(self):
        a = [4, 2, 6, 3, 5, 7, 1, 9]
        self.add_testcase(a, sorted(a))

    def solve(self, test_in):
        return self.quicksort(test_in)
