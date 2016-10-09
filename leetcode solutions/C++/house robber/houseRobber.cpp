class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() == 0)
                return 0;

        int value1 = nums[0];

        if (nums.size() == 1)
            return value1;

        int value2 = max(value1, nums[1]);

        if (nums.size() == 2)
            return max(value1, value2);

        int value = 0;

        for (int i = 2; i < nums.size(); i++) {
            value = max(value2, value1 + nums[i]);
            value1 = value2;
            value2 = value;
        }
        return value;
    }
};