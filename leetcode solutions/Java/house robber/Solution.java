public class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0)
            return 0;

        int value1 = nums[0];

        if (nums.length == 1)
            return value1;

        int value2 = Math.max(value1, nums[1]);

        if (nums.length == 2)
            return Math.max(value1, value2);

        int value = 0;

        for (int i = 2; i < nums.length; i++) {
            value = Math.max(value2, value1 + nums[i]);
            value1 = value2;
            value2 = value;
        }
        return value;

    }
}