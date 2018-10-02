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

未实现！！！！！
"""


class Hash:
    def __init__(self):
        self.capacity = 11
        self.hash_table = [[None, None] for i in range(self.capacity)]
        self.num = 0
        self.load_factor = 0.75

    def hash(self, k, i):
        h_value = (k + i) % self.capacity
        if self.hash_table[h_value][0] == k:
            return h_value
        if self.hash_table[h_value][0] != None:
            i += 1
            h_value = self.hash(k, i)
        return h_value

    def resize(self):
        #扩容到原有元素数量的两倍
        self.capacity = self.num * 2
        temp = self.hash_table[:]
        self.hash_table = [[None, None] for i in range(self.capacity)]
        for i in temp:
            #把原来已有的元素存入
            if (i[0] != None):
                hash_v = self.hash(i[0], 0)
                self.hash_table[hash_v][0] = i[0]
                self.hash_table[hash_v][1] = i[1]

    def put(self, k, v):
        hash_v = self.hash(k, 0)
        self.hash_table[hash_v][0] = k
        self.hash_table[hash_v][1] = v
        #暂不考虑key重复的情况，具体自己可以优化
        self.num += 1
        # 如果比例大于载荷因子
        if (self.num / len(self.hash_table) > self.load_factor):
            self.resize()

    def get(self, k):
        hash_v = self.hash(k, 0)
        return self.hash_table[hash_v][1]


class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_obj = Hash()
        for k, v in enumerate(nums):
            if hash_obj.get(target - v):
                for ik, iv in enumerate(nums):
                    if iv == target - v:
                        return [k, ik]
            hash_obj.put(v, v)
        return False


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution()
        res = obj.twoSum([2, 7, 11, 15], 9)
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
