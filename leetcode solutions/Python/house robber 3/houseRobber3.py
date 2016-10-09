class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.robHelper(root)
        return max(res[0], res[1])


    def robHelper(self, root):
        if not root:
            return [0,0]

        left = self.robHelper(root.left)
        right = self.robHelper(root.right)

        res = [0,0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]

        return res