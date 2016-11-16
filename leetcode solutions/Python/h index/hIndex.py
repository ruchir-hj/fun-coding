# Time:  O(n)
# Space: O(n)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        counting_sort_arr = [0] * (len(citations) + 1)
        for citation in citations:
            if citation >= len(counting_sort_arr):
                counting_sort_arr[-1] += 1
            else:
                counting_sort_arr[citation] += 1

        h = 0
        for i in xrange(len(counting_sort_arr) - 1, 0 , -1):
            h += counting_sort_arr[i]
            if h >= i:
                return i

        return 0



# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h