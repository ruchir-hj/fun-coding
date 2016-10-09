class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(self.robHelper(nums, 0, n - 2), self.robHelper(nums, 1, n -1))


    def robHelper(self, nums, start, end):
        pre = 0
        cur = 0

        for i in xrange(start, end+1):
            value = max(pre + nums[i], cur)
            pre = cur
            cur = value

        return cur