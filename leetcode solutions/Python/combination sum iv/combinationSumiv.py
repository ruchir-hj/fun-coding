class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        combs = [0] * (target + 1)
        combs[0] = 1

        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    combs[i] += 1

                if num < i:
                    combs[i] += combs[i - num]
        return combs[target]