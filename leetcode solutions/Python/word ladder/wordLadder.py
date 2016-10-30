class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        distance, cur, visited = 0, [beginWord], set([beginWord])
        wordList.add(endWord)

        while cur:
            next = []
            for word in cur:
                if word == endWord:
                    return distance + 1

                for i in range(0, len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in wordList:
                            next.append(candidate)
                            visited.add(candidate)

            distance += 1
            cur = next
        return 0