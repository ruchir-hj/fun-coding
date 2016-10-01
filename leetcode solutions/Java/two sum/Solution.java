public class Solution {
    public int[] twoSum (int[] nums, int target) {
        HashMap<Integer, Integer> lookup = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int b = target - nums[i];

            if (lookup.get(b) != null) {
                return new int[] {lookup.get(b), i};
            }
            else {
                lookup.put(nums[i], i);
            }
        }
        return null;

    }
}