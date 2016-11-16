class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start = 0
        end = len(citations) - 1
        length = len(citations)

        while start <= end:
            mid = start + (end - start)/2
            if citations[mid] >= length - mid:
                end = mid - 1
            else:
                start = mid + 1

        return length - start
