from pingcode.util import Problem

class MinimumNumberOfConsecutiveBitflip(Problem):
    def leetcode_id(self):
        return 995

    def description(self):
        return """Given nums containing only 0s and 1s. You are only allowed to flip 'k consecutive bits' and
                  the goal is to flip the entire array into 1s"""

    def observations(self):
        return ["when encountering a zero, flip it greedily is ok.",
                "Each index flip at most once"]

    def min_number_of_k_consecutive_bitflip(self, nums, k):
        total_flips = 0

        curr_flips = 0
        flipped = [False] * len(nums)
        for i in range(len(nums)):
            if i >= k and flipped[i - k]:
                curr_flips -= 1

            # if encounter a zero and neither is it flipped or
            # if encounter an one and it has flipped.
            if (curr_flips % 2) ^ nums[i] == 0:
                if i + k > len(nums):
                    return -1
                curr_flips += 1
                total_flips += 1
                flipped[i] = True

        return total_flips

    def import_testcases(self):
        test_in = ([0, 1, 0], 1)
        self.add_testcase(test_in, 2)

        test_in = ([1, 1, 0], 2)
        self.add_testcase(test_in, -1)

        test_in = ([0,0,0,1,0,1,1,0], 3)
        self.add_testcase(test_in, 3)

    def solve(self, test_in):
        nums, k = test_in
        return self.min_number_of_k_consecutive_bitflip(nums, k)

