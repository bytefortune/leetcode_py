# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""


class Solution:
    def __init__(self):
        pass

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_minus = False
        if int(x) < 0:
            is_minus = True
            x = -x
        res = 0
        while x:
            tmp = res * 10 + x % 10
            if tmp // 10 != res or tmp > 2**31 - 1:
                return 0
            res = tmp
            x = x // 10
        if is_minus:
            res = -res
        return res


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution()
        res = obj.reverse(-120)
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
