class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        mem = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n not in mem:
                mem.add(n)
            else:
                return False
        return True



# solution 2 : more elegant but TLE

'''
class Solution:

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {}
        while n != 1 or n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1


    def nextNumber(self, n):
        new = 0
        for ch in str(n):
            new += int(ch) ** 2
        return new
'''