import collections

from pingcode.util import Problem


class NumNiceSubarray(Problem):
    def leetcode_id(self):
        return 1248

    def description(self):
        return """
                Given an array of integer and a number k, a nice subarray is defined as an subarray with exact k odd number
               """

    def num_of_nice_subarray(self, nums, k):
        return self.subarray_at_most_k_odd(nums, k) - self.subarray_at_most_k_odd(nums, k - 1)

    def subarray_at_most_k_odd(self, nums, k):
        num_subarray = 0
        start = 0
        curr_odd = 0
        # sliding window
        for end, num in enumerate(nums):
            # slient store for num is even
            curr_odd += num % 2

            while curr_odd > k:
                curr_odd -= nums[start] % 2
                start += 1

            # add [start, end], [start + 1, end], ..., [end, end]
            num_subarray += end - start + 1

        return num_subarray

    def import_testcases(self):
        test_in = ([1,1,2,1,1], 3)
        self.add_testcase(test_in, 2)
        test_in = ([2,2,2,1,2,2,1,2,2,2], 2)
        self.add_testcase(test_in, 16)
        test_in = ([94, 77, 7, 35, 26, 7, 23, 61, 51, 47, 99, 45, 62, 98, 12, 96, 20, 39, 62, 30, 9, 9, 98, 83, 69, 40, 18, 8, 23, 65, 20, 88, 21, 78, 51, 93, 36, 55, 6, 85, 36, 20, 50, 60, 13, 90, 80, 14, 92, 77, 30, 29, 34, 17, 35, 17, 48, 97, 77, 19, 20, 19, 67, 86, 28, 78, 2, 54, 78, 76, 88, 9, 85, 97, 24, 36, 63, 20, 4, 4, 37, 47, 1, 36, 69, 77, 81, 64, 14, 19, 64, 48, 71, 36, 40, 78, 1, 66, 12, 38], 20)
        self.add_testcase(test_in, 128)

    def solve(self, test_in):
        nums, k = test_in
        return self.num_of_nice_subarray(nums, k)

class TotalSubarrayWithExactKDistinctInteger(Problem):
    def subarray_with_k_distinct(self, nums, k):
        return (self.subarray_with_at_most_k(nums, k) -
                self.subarray_with_at_most_k(nums, k - 1))

    def subarray_with_at_most_k(self, nums, k):
        total_subarray = 0
        frequency = collections.Counter()

        start = 0
        distinct = 0
        for end, num in enumerate(nums):
            frequency[num] += 1
            if frequency[num] == 1:
                distinct += 1

            while distinct > k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == 0:
                    distinct -= 1
                start += 1

            total_subarray += end - start + 1

        return total_subarray


    def import_testcases(self):
        test_in = ([1,2,1,2,3], 2)
        self.add_testcase(test_in, 7)

        test_in = ([1,2,1,3,4], 3)
        self.add_testcase(test_in, 3)


    def solve(self, test_in):
        nums, k = test_in
        return self.subarray_with_k_distinct(nums, k)


