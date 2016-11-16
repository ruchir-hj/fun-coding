class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n < 2:
            return n

        id = 1

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[id] = nums[i]
                id += 1
        nums = nums[:id]
        return id

