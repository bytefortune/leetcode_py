# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, node_str):
        self.node_list = node_str.split("->")
        self.head = ListNode(self.node_list[0])
        p = self.head
        for i in self.node_list[1:]:
            node = ListNode(i)
            p.next = node
            p = node

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while 1:
            if p and p.next:
                if p.val == p.next.val:
                    p.next = p.next.next
                if p.next and p.val != p.next.val:
                    p = p.next
            else:
                break

        return head


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution("1->1->1")
        res = obj.deleteDuplicates(obj.head)
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
