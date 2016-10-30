class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numsToPosMap = {}
        self.nums = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.numsToPosMap:
            self.nums.append(val)
            self.numsToPosMap[val] = len(self.nums) - 1
            return True
        return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.numsToPosMap:
            pos = self.numsToPosMap[val]
            self.nums[pos], self.nums[len(self.nums) - 1] = self.nums[len(self.nums) - 1], self.nums[pos]
            self.numsToPosMap[self.nums[pos]] = pos
            del self.numsToPosMap[val]
            self.nums.pop()
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) -  1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()