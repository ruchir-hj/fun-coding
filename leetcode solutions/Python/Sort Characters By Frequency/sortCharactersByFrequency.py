import collections

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return ''

        char_to_count_map = collections.defaultdict(int)

        for chr in s:
            char_to_count_map[chr] += 1

        counting_sort_arr = [[] for _ in xrange(len(s) + 1)]

        for k, v in char_to_count_map.iteritems():
            counting_sort_arr[v].append(k)

        res = []
        for i in range(len(counting_sort_arr) - 1, -1, -1):
            if counting_sort_arr[i] != []:
                temp = sorted(counting_sort_arr[i])
                for j in range(len(temp)):
                    for k in range(i):
                        res.append(temp[j])

        return ''.join(res)



