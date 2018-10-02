# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.dirname(os.getcwd()))
from solution import removeElement


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = removeElement.Solution()
        res = obj.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
