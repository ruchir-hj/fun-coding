public class Solution {
    public int romanToInt(String s) {

        if (s.isEmpty()) return 0;

        Map<Character, Integer> romeToNatural = new HashMap<Character, Integer>();
        romeToNatural.put('I', 1);
        romeToNatural.put('V', 5);
        romeToNatural.put('X', 10);
        romeToNatural.put('L', 50);
        romeToNatural.put('C', 100);
        romeToNatural.put('D', 500);
        romeToNatural.put('M', 1000);

        int total = 0, preValue = 0;

        for (int i =0; i < s.length(); i++) {
            Integer value = romeToNatural.get(s.charAt(i));

            if (value <= preValue)
                total += value;
            else
                total += value - 2 * preValue;

            preValue = value;
        }

    return total;
    }
}