# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def __init__(self):
        pass

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_map = {"}": "{", "]": "[", ")": "("}
        stack_list = []
        for i in s:
            if stack_list:
                if i in ['(', '[', '{']:
                    stack_list.append(i)
                else:
                    if char_map[i] == stack_list[-1]:
                        stack_list.pop()
                    else:
                        stack_list.append(i)
            else:
                stack_list.append(i)
        return len(stack_list) == 0


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution()
        res = obj.isValid('[([][[]])]')
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
