#!/usr/bin/env python3

import heapq
import random

from pingcode.util import Problem


class DreamTeam(Problem):
    def select_dream_team_member(self, k, teams):
        candidate_teams = self.qselect(k, teams)
        pq = [(team[0], team, 0) for team in candidate_teams]
        heapq.heapify(pq)

        dream_team = []
        while pq:
            player, team, idx = heapq.heappop(pq)
            dream_team.append(player)
            if len(dream_team) == k:
                break
            if idx + 1 < len(team):
                heapq.heappush(pq, (team[idx + 1], team, idx + 1))

        return dream_team

    def qselect(self, k, teams):
        if k >= len(teams):
            return teams

        idx = random.randint(0, len(teams) - 1)
        pivot_team = teams[idx]

        left = [team for team in teams if team <= pivot_team]
        if k <= len(left):
            return self.qselect(k, left)

        right = [team for team in teams if team > pivot_team]
        return left + self.qselect(k - len(left), right)

    def import_testcases(self):
        test_in = (4, [[1, 5, 7, 9], [2, 4, 8, 10], [0, 3, 6, 9]])
        test_out = [0, 1, 2, 3]
        self.add_testcase(test_in, test_out)

        test_in = (2, [[16, 18], [0, 10], [5, 7], [2, 9],
                       [11, 19], [8, 17], [6, 13], [1, 11],
                       [14, 16], [1, 4]])
        test_out = [0, 1]
        self.add_testcase(test_in, test_out)

    def solve(self, test_in):
        k, teams = test_in
        return self.select_dream_team_member(k, teams)
