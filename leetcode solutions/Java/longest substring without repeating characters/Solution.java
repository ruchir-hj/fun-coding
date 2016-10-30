public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int end = 0;
        int maxLength = 0;

        HashMap<Character, Integer> usedChars = new HashMap<Character, Integer>();

        while (end < s.length()) {
            if ((usedChars.get(s.charAt(end)) != null) && (start <= usedChars.get(s.charAt(end))))
                start = usedChars.get(s.charAt(end)) + 1;
            else
                maxLength = Math.max(maxLength, end - start + 1);

            usedChars.put(s.charAt(end), end);
            end++;


        }
        return maxLength;
    }
}