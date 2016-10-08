public class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0 || s.charAt(0) == '0')
            return 0;

        int prev = 1, prevPrev = 1;
        int cur;

        for (int i = 0; i < s.length(); i++) {
            cur = 0;

            if (s.charAt(i) != '0')
                cur = prev;

            if ((i > 0) && ((s.charAt(i -1) == '1') || (s.charAt(i - 1) == '2' && s.charAt(i) <= '6')))
                cur += prevPrev;

            prevPrev = prev;
            prev = cur;
        }

        return prev;
    }
}