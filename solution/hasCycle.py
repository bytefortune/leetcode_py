# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while fast.next is not None and fast.next.next is not None:
            if fast.next == slow.next:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False


# class Run(object):
#     def __init__(self):
#         pass

#     def run_interface(self):
#         obj = Solution()
#         res = obj.hasCycle(obj.head)
#         print(res)


# if __name__ == '__main__':
#     run = Run()
#     run.run_interface()
