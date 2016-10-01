class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print board
        seen = set()

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):

                if board[i][j] != '.':
                    curr = '(' + str(board[i][j]) + ')'

                    if curr+str(i) in seen or str(j) + curr in seen or str(i/3) + curr + str(j/3) in seen:
                        return False

                    seen.add(curr+str(i))
                    seen.add(str(j) + curr)
                    seen.add(str(i/3) + curr + str(j/3))

        return True