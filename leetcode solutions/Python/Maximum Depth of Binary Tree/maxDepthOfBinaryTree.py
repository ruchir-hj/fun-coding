class TreeNode:
    def __init__(self):
        self.val = x
        self.left = None
        self.right = None


class Solution(Object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, node, depth):
        if not node:
            return depth

        return max(self.maxDepthHelper(node.left, depth + 1), self.maxDepthHelper(node.right, depth + 1))
