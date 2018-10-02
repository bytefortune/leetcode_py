# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.dirname(os.getcwd()))
from solution import leafSimilar


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = leafSimilar.Solution(
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        res = obj.leafSimilar(obj.node_list1[0], obj.node_list2[0])
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
