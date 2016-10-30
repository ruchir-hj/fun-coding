class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in range(len(nums) + 1)]
        frequencyMap = collections.defaultdict(int)

        for num in nums:
            frequencyMap[num] += 1

        for key in frequencyMap.keys():
            bucket[frequencyMap[key]].append(key)

        res = []

        while k > 0:
            for pos in range(len(bucket) -1 , -1, -1):

                if bucket[pos] != []:
                    for item in bucket[pos]:
                        if k == 0:
                            break
                        k -= 1
                        res.append(item)


        return res

