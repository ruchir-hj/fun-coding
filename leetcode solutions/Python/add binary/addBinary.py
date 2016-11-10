class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = ''

        while i >= 0 or j >= 0 or carry:
            sum = 0

            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:
                sum += int(b[j])
                j -= 1

            if carry:
                sum += carry

            carry = sum / 2
            sum = sum % 2
            res += str(sum)

        return res[::-1]

