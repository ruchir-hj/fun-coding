class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        value1 = nums[0]

        if len(nums) == 1:
            return value1

        value2  = max(value1, nums[1])

        if len(nums) == 2:
            return max(value1, value2)

        for i in xrange(2, len(nums)):
            value = max(value2, value1 + nums[i])
            value1 = value2
            value2 = value

        return value

