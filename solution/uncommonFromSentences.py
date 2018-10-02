# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。

 

示例 1：

输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
示例 2：

输入：A = "apple apple", B = "banana"
输出：["banana"]
 

提示：

0 <= A.length <= 200
0 <= B.length <= 200
A 和 B 都只包含空格和小写字母。
"""


class Solution:
    def __init__(self):
        pass

    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ret = []
        list_c = A.split() + B.split()
        for word in set(list_c):
            num = list_c.count(word)
            if num == 1:
                ret.append(word)
        return ret


class Run(object):
    def __init__(self):
        pass

    def run_interface(self):
        obj = Solution()
        res = obj.uncommonFromSentences(
            "xfj vcahm vcahm frkqt oibcc jko oibcc frkqt ft tr",
            "lv ktx ktx tr x xfj xfj frkqt ktx ta tr yynk vcahm")
        print(res)


if __name__ == '__main__':
    run = Run()
    run.run_interface()
