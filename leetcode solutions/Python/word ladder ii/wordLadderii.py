class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        wordList.add(beginWord)
        wordList.add(endWord)

        result, cur, visited, found, trace = [], [beginWord], set([beginWord]), False, {word : [] for word in wordList}

        while cur and not found:
            for word in cur:
                visited.add(word)

            next = set()
            for word in cur:
                for i in range(0, len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]

                        if candidate not in visited and candidate in wordList:
                            if candidate == endWord:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next

        if found:
            self.backtrack(result, trace, [], endWord)

        return result




    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)
