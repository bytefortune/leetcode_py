# !/usr/bin/env python
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
"""
请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

提示：

给定的两颗树可能会有 1 到 100 个结点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self, data1, data2):
        pass
        # self.root = TreeNode(data[0])
        self.node_list1 = self.initTree(data1)
        self.node_list2 = self.initTree(data2)
        # for i in range((len(data) - 2) / 2):

        #     p = p.left

    def initTree(self, data):
        node_list = []
        for i in data:
            node_list.append(TreeNode(i))

        level = 1

        while True:
            break_flag = True
            # 只要有一个不为空，说明当前层级存在，不跳出
            for i in data[2**level - 1:2**(level + 1) - 1]:
                if i:
                    break_flag = False
            if break_flag:
                break

            for i, v in enumerate(node_list[2**(level - 1) - 1:2**level - 1]):
                if (2**(level - 1) - 1 + i) * 2 + 1 < len(
                        node_list) and node_list[(2**(level - 1) - 1 + i) * 2
                                                 + 1].val:
                    v.left = node_list[(2**(level - 1) - 1 + i) * 2 + 1]
                if (2**(level - 1) - 1 + i) * 2 + 2 < len(
                        node_list) and node_list[(2**(level - 1) - 1 + i) * 2
                                                 + 2].val:
                    v.right = node_list[(2**(level - 1) - 1 + i) * 2 + 2]
            level += 1
        for i in node_list:
            print(type(i))
            print(i.val)
        return node_list

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(node):
            if node:
                if (not node.left and not node.right and node.val):
                    yield node.val
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)

        list1 = list(dfs(root1))
        list2 = list(dfs(root2))
        return list1 == list2


# if __name__ == '__main__':
#     run = Run()
#     run.run_interface()
