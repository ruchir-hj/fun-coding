public class Solution {
    public int findMaximumXOR(int[] nums) {
        int max = 0, mask = 0;
        for (int i = 31; i >= 0; i--) {
            mask = mask | (1 << i);
            Set<Integer> prefixSet = new HashSet<>();

            for (int num : nums) {
                prefixSet.add(num & mask);
            }
            int tmp = max | (1 << i);
            for (int prefix : prefixSet) {
                if (prefixSet.contains(tmp ^ prefix)) {
                    max = tmp;
                    break;
                }
            }
        }
        return max;
    }
}