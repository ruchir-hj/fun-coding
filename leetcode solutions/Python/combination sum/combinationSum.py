class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSumHelper(sorted(candidates), target, result, [], 0)
        return result


    def combinationSumHelper(self, candidates, target, result, current, start):
        if target == 0:
            result.append(list(current))
            return

        while start < len(candidates) and candidates[start] <= target:
            current.append(candidates[start])
            self.combinationSumHelper(candidates, target - candidates[start], result, current, start)
            current.pop()
            start += 1


