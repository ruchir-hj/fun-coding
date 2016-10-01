#include <iostream>

using namespace std;
//const int N = 0;

class Solution {
public:
    int titleToNumber (string s) {
        int colNum = 0;
        for (char i : s) {
            colNum = colNum * 26 + (i - 'A' + 1);
        }
        return colNum;
    }


};

int main() {
    string str;
    Solution s;
    while (cin >> str)
        cout << s.titleToNumber(str) << endl;
    return 0;
}