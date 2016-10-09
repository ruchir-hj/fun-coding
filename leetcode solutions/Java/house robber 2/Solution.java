public class Solution {
    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 0)
            return 0;

        if (n == 1)
            return nums[0];

        return Math.max(robHelper(nums, 0, n-2), robHelper(nums, 1, n-1));
    }

    private int robHelper(int[] nums, int start, int end) {
        int pre = 0, cur = 0;

        for (int i = start; i <= end; i++) {
            int value = Math.max(pre + nums[i], cur);
            pre = cur;
            cur = value;
        }
        return cur;
    }
}