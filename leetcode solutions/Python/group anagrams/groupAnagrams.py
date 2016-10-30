from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        res = []

        for s in strs:
            k = self.form_key(s)
            d[k].append(s)

        for k in d:
            res.append(sorted(d[k]))

        return res


    def form_key(self, s):
        return ''.join(sorted(s))



