#!/usr/bin/env python3

from pingcode.util import Problem


class MergeSort(Problem):
    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])

        merged = []
        i = j = 0
        while i < len(left):
            if j >= len(right) or left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged += right[j:]

        return merged

    def import_testcases(self):
        a = [4, 2, 6, 3, 5, 7, 1, 9]
        self.add_testcase(a, sorted(a))

    def solve(self, test_in):
        return self.mergesort(test_in)
