public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        Map<String, List<String>> groups = new HashMap<>();

        for (int i = 0; i< strings.length; i++) {
            String key = hashStr(strings[i]);
            if (groups.containsKey(key)) {
                groups.get(key).add(strings[i]);
            } else {
                groups.put(key, new ArrayList<String>());
                groups.get(key).add(strings[i]);
            }
        }

        List<List<String>> result = new ArrayList<>();

        for (String key : groups.keySet()) {
            List<String> g = groups.get(key);
            Collections.sort(g);
            result.add(g);
        }
        return result;
    }

    public String hashStr(String s) {
        String key = "";
        for (int i = 1; i < s.length(); i++) {
            int diff = (int) (s.charAt(i) - s.charAt(i-1));
            if (diff < 0) {diff += 26;}
            key += 'a' + diff;
        }
        return key;
    }
}