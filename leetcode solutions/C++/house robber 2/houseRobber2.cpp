class Solution {
public:
    int rob (vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;

        if (n == 1)
            return nums[0];

        return max(robHelper(nums, 0, n-2), robHelper(nums, 1, n-1));
    }

private:
    int robHelper(vector<int>& nums, int start, int end) {
        int pre = 0, cur = 0;

        for (int i = start; i <=end; i++) {
            int value = max(pre + nums[i], cur);
            pre = cur;
            cur = value;
        }
        return cur;
    }
};