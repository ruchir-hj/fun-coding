class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string> > groups;
        vector<vector<string>> groupsVec;

        for (string s : strings)
            groups[hashstr(s)].push_back(s);



        for (auto g : groups) {
            vector<string> group = g.second;
            sort(group.begin(), group.end());
            groupsVec.push_back(group);
        }
        return groupsVec;


    }

private:
    string hashstr(string& s) {
        string hashcode;
        int n = s.length();
        for (int i = 1; i < n; i ++) {
            int diff = s[i] - s[i-1];
            if (diff < 0) diff += 26;
            hashcode += 'a' + diff;
        }
        return hashcode;
    }
};