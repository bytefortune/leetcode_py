# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for k, i in enumerate(nums):
            if target - i in nums[k + 1:]:
                return [k, nums[k + 1:].index(target - i) + k + 1]


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution()
        res = obj.twoSum([3, 0, 0, 3], 0)
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
