#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum (vector<int>& nums, int target) {
        unordered_map<int, int> lookup;
        vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int numberToFind = target - nums[i];

            if (lookup.find(numberToFind) != lookup.end()) {
                result.push_back(lookup[numberToFind]);
                result.push_back(i);
                return result;
            }
            lookup[nums[i]] = i;
        }
        return result;
    }
};