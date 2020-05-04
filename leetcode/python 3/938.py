# 문제 링크: https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(root: TreeNode):
            if not root:
                return 0

            sum_val = 0
            if root.val >= L and root.val <= R:
                sum_val += root.val
            if root.val > L:
                sum_val += dfs(root.left)
            if root.val < R:
                sum_val += dfs(root.right)
            return sum_val

        return dfs(root)
