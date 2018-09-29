# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.dirname(os.getcwd()))
from solution import isPalindrome


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = isPalindrome.Solution()
        res = obj.isPalindrome(121)
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
