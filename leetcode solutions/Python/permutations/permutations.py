class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        used = [False] * len(nums)
        self.permuteHelper(result, used, [], nums)
        return result

    def permuteHelper(self, result, used, cur, nums):
        if len(cur) == len(nums):
            result.append(cur + [])
            return

        for i in xrange(len(nums)):
            if not used[i]:
                used[i] = True
                cur.append(nums[i])
                self.permuteHelper(result, used, cur, nums)
                cur.pop()
                used[i] = False


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permuteHelper(nums, result, 0)
        return result

    def permuteHelper(self, nums, result, i):
        if i == len(nums):
            result.append(nums)
            return

        for j in xrange(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.permuteHelper(nums, result, i + 1)
            nums[i], nums[j] = nums[j], nums[i]



