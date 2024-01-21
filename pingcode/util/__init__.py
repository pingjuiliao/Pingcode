#!/usr/bin/env python3

class Problem(object):
    def __init__(self):
        self.solutions = []
        self.testcases = []

    def add_testcase(self, test_in, test_out):
        self.testcases.append((test_in, test_out))


    def evaluate(self):
        passed = 0
        for i, o in self.testcases:
            my_solve = self.solve(i)
            print("###################################")
            print(f"Input: {i}")
            print(f"Output: {my_solve}")
            print(f"Expected: {o}")
            if my_solve == o:
                print("[Correct]")
                passed += 1
            else:
                print("[Wrong Answer]")
        print("################################")
        print(f"##### {passed}/{len(self.testcases)} passed ##########")
        print("################################")

    def solve(self, test_input):
        raise "No solution implemented"
