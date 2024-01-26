#!/usr/bin/env python3

import argparse


algorithm_list = {
    'num_bst': 'pingcode.dynamic_programming.catalan.NumBST',
    'knapsack1': 'pingcode.dynamic_programming.knapsack.KnapsackUnboundedProduct',
    'knapsack2': 'pingcode.dynamic_programming.knapsack.KnapsackBoundedProduct',
    'mis': 'pingcode.dynamic_programming.max_independent_set.MaxIndependentSet',
    'bitstring': 'pingcode.dynamic_programming.string_combination.BitstringNoConsecutiveOnes',
    'dijkstra': 'pingcode.graph.shortest_path.ShortestPath',
    'tsp': 'pingcode.graph.tsp.TravelingSalesman',
    'kbest_pair': 'pingcode.kbest.kbest_pair.KBestPairFromTwoList',
    'dream_team': 'pingcode.kbest.dream_team.DreamTeam',
    'mergesort': 'pingcode.sorting.mergesort.MergeSort',
    'quicksort': 'pingcode.sorting.quicksort.QuickSort',
}


def algorithm_class_import(name):
    module_name, alg_class_name = name.rsplit('.', 1)
    module = __import__(module_name, fromlist=[alg_class_name])
    alg_class = getattr(module, alg_class_name)
    return alg_class


def parse_args():
    p = argparse.ArgumentParser(prog='run.py')
    arg_action_group = p.add_mutually_exclusive_group(required=True)
    arg_action_group.add_argument('-a', '--alg', dest='algorithm')
    arg_action_group.add_argument('-l', '--list', action='store_true')
    args = p.parse_args()

    if args.list:
        print('Available options:')
        for k in algorithm_list.keys():
            print(f'= {k} |')
        return
    # mutually exclusive group should
    assert(args.algorithm is not None)
    run_algorithm(args)

def run_algorithm(args):
    if args.algorithm not in algorithm_list:
        print(f'[Error] {args.algorithm} not found.')
        return

    module_name = algorithm_list[args.algorithm]

    # (Dynamically) Get the class
    AlgorithmProblem = algorithm_class_import(module_name)

    # Problem & Solve
    problem = AlgorithmProblem()
    problem.evaluate()


if __name__ == '__main__':
    parse_args()
