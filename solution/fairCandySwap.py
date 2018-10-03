# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。

因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。

 

示例 1：

输入：A = [1,1], B = [2,2]
输出：[1,2]
示例 2：

输入：A = [1,2], B = [2,3]
输出：[1,2]
示例 3：

输入：A = [2], B = [1,3]
输出：[2,3]
示例 4：

输入：A = [1,2,5], B = [2,4]
输出：[5,4]
 

提示：

1 <= A.length <= 10000
1 <= B.length <= 10000
1 <= A[i] <= 100000
1 <= B[i] <= 100000
保证爱丽丝与鲍勃的糖果总量不同。
答案肯定存在。

题解：
设爱丽丝和鲍勃分别总计有 S_A, S_B的糖果


如果爱丽丝给了糖果 x，并且收到了糖果 y，那么鲍勃收到糖果 x 并给出糖果 y。那么，我们一定有

S_A - x + y = S_B - y + x
"""


class Solution:
    def __init__(self):
        pass

    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a, sum_b = sum(A), sum(B)
        setB = set(B)
        for i in A:
            j = int((sum_b - sum_a) / 2 + i)
            if j in setB:
                return (i, j)


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution()
        res = obj.fairCandySwap([1, 1], [2, 2])
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
