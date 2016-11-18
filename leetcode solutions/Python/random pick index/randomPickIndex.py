class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums



    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        reservoir = -1
        n = 0

        for i in xrange(len(self.nums)):
            if self.nums[i] != target:
                continue
            if n == 0 or random.randint(1, n+1) == 1:
                reservoir = i
            n += 1

        return reservoir




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)