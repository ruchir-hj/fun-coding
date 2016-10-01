public class Solution {
    public int titleToNumber(String s) {

        int colNum = 0;

        for (int i = 0; i < s.length(); i++) {
            colNum = colNum * 26 + (s.charAt(i) - 'A' + 1);
        }

        return colNum;
    }

    public static void main(String[] args) {

        Scanner cin = new Scanner(System.in);
        Solution s = new Solution();
        System.out.println(s.titleToNumber("AB"));
    }
}