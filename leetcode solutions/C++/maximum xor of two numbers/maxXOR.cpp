class Solution {
public:
    int findMaximumXOR (vector<int>& nums) {
        int max = 0, mask = 0;
        unordered_set<int> prefixSet;

        for (int i = 31; i >= 0; i--) {
            mask |= (1 << i);
            prefixSet.clear();

            for (int num: nums) {
                prefixSet.insert(mask & num);
            }

            int candidate = max | (1<<i);

            for (int prefix : prefixSet) {
                if (prefixSet.find(prefix ^ candidate) != prefixSet.end()) {
                    max = candidate;
                    break;
                }
            }
        }
        return max;
    }
};