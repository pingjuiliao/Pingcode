#!/usr/bin/env python3

import argparse
from pingcode.sorting.quicksort import QuickSort


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('-a', '--alg', dest='algorithm', required=True)
    args = p.parse_args()

    print(args.algorithm)

    if args.algorithm == 'quicksort':
        print("solving quicksort")
        qsort = QuickSort()
        qsort.evaluate()



if __name__ == '__main__':
    parse_args()
