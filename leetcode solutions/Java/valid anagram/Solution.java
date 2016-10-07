// array acting as a map solution

public class Solution {
    public boolean isAnagram(String s, String t) {
        int[] alphabet = new int[26];

        for (int i = 0; i < s.length(); i++)
            alphabet[s.charAt(i)  - 'a']++;

        for (int i = 0; i < t.length(); i++)
            alphabet[t.charAt(i) - 'a']--;

        for (int count : alphabet)
            if (count != 0)
                return false;

        return true;

    }
}

// sorting O(nlogn)

public class Solution {
    public boolean isAnagram(String s, String t) {
        char[] schar = s.toCharArray();
        char[] tchar = t.toCharArray();

        Arrays.sort(schar);
        Arrays.sort(tchar);

        s = new String(schar);
        t = new String(tchar);

        return s.equals(t);
    }
}