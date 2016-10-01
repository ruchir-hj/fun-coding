#include <iostream>
#include <set>

using namespace std;

class Solution {
public:
    bool canPermutePalindrome(string s) {

        if (s.length() == 0) {
            return false;
        }
        set<char> chSet;

        for (int i =0; i < s.length(); i++) {
            if (chSet.find(s[i])==chSet.end())
                chSet.insert(s[i]);
            else
                chSet.erase(s[i]);
        }

        if (s.length() % 2 == 0)
            return (chSet.size() == 0);
        else
            return (chSet.size() == 1);
    }
};