class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = []

        for i in range(0, len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

        for i in range(0, len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res