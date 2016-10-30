class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))








# alternate solution



class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.strip()

        if not s:
            return ""

        message_list = list(s)

        self.reverse_characters(message_list, 0, len(message_list) - 1)

        current_word_start_index = 0

        i = 0
        for i in range(0, len(message_list) + 1):

            if i == len(message_list) or message_list[i] == ' ':
                self.reverse_characters(message_list, current_word_start_index, i - 1)

            current_word_start_index = i+1

            i += 1

        return ''.join(message_list)


    def reverse_characters(self, message_list, start, end):
        while start < end:
            message_list[start], message_list[end] = message_list[end], message_list[start]

            start += 1
            end -= 1

        return message_list