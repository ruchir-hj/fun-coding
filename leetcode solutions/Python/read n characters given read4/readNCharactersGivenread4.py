# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read_bytes = 0
        buffer = [''] * 4
        for i in range(n/4 + 1):
            size = read4(buffer)
            if size:
                buf[read_bytes:read_bytes+size] = buffer
                read_bytes += size
            else:
                break
        return min(read_bytes, n)
