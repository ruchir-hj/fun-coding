class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        unordered_map<char, int> countMap;

        for (int i =0; i < n; i++) {
            countMap[s[i]]++;
            countMap[t[i]]--;
        }

        for (auto count : countMap)
            if (count.second) return false;
        return true;
    }
};



// sorting
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(), s.end());
        sort(t.begin(), s.end());
        return s == t;
    }
};