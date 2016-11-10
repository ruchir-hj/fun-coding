# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.sumOfLeftLeavesHelper(root, False)

    def sumOfLeftLeavesHelper(self, root, is_left):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val if is_left else 0

        return self.sumOfLeftLeavesHelper(root.left, True) + self.sumOfLeftLeavesHelper(root.right, False)