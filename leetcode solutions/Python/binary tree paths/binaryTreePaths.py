# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []

        res = []
        path = [root.val]
        self.binaryTreePathsHelper(root, path, res)
        return res

    def binaryTreePathsHelper(self, root, path, res):
        if not root.left and not root.right:
            res.append('->'.join(str(x) for x in path))
            return

        if root.left:
            self.binaryTreePathsHelper(root.left, path + [root.left.val], res)

        if root.right:
            self.binaryTreePathsHelper(root.right, path + [root.right.val], res)



