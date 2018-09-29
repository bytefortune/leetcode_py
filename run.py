# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.dirname(os.getcwd()))
from solution import middleNode


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        self.initlist([1, 2, 3, 4, 5])
        obj = middleNode.Solution()
        res = obj.middleNode(self.head)
        print(res.val)

    def initlist(self, data):

        self.head = middleNode.ListNode(data[0])

        p = self.head

        for i in data[1:]:
            node = middleNode.ListNode(i)
            p.next = node
            p = p.next


if __name__ == '__main__':
    run = Run()
    run.run_interface()
