public class Solution {
    public boolean canPermutePalindrome(String s) {

        if (s.length() == 0) {
            return false;
        }
        Set<Character> set = new HashSet<Character>();

        for (int i = 0; i < s.length(); i++) {
            if (!set.contains(s.charAt(i))) {
                set.add(s.charAt(i));
            }
            else {
                set.remove(s.charAt(i));

            }
        }
        if (s.length() % 2 == 0)
            return set.size() == 0;
        else
            return set.size() == 1;
    }
}