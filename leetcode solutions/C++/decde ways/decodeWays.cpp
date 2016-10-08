class Solution {
public:
    int numDecodings(string s) {
        if (!s.size() || s.front() == '0') return 0;

        int prev = 1, prev_prev = 1;
        int cur;

        for (int i = 0; i < s.size(); i++) {
            cur = 0;

            if (s[i] != '0')
                cur = prev;

            if ((i > 0) && ((s[i - 1] == '1') || (s[i-1] == '2' && s[i] <= '6')))
                cur += prev_prev;

            prev_prev = prev;
            prev = cur;

        }
        return prev;
    }


};