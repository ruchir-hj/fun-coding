class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSum2Helper(sorted(candidates), target, result, [], 0)
        return result


    def combinationSum2Helper(self,candidates, target, result, current, start):
        if target == 0:
            result.append(list(current))
            return
        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]:
                current.append(candidates[start])
                self.combinationSum2Helper(candidates, target - candidates[start], result, current, start + 1)
                current.pop()
                prev = candidates[start]
            start += 1
