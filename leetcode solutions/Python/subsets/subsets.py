
# bit manipulation
class Solution(object):
    def subsets(self, nums):
        nums.sort()
        total = 2 ** len(nums)
        res = []

        for i in xrange(total):
            res.append([])

        for i in xrange(len(nums)):
            for j in xrange(total):
                if ((j>>i)&1) > 0:
                    res[j].append(nums[i])

        return res


# recursion
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsHelper([], sorted(nums))


    def subsetsHelper(self, curr, nums):
        if not nums:
            return [curr]

        return self.subsetsHelper(curr, nums[1:]) + self.subsetsHelper(curr + [nums[0]], nums[1:])

# iteration
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]

        for i in xrange(len(nums)):
            size = len(result)
            for j in xrange(size):
                 result.append(list(result[j]))
                 result[-1].append(nums[i])
        return result
