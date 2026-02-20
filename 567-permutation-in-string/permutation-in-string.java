class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) return false;

        HashMap<Character, Integer> map1 = new HashMap<>(), map2 = new HashMap<>();

        for (int i = 0; i < n1; i++) {
            map1.put(s1.charAt(i), map1.getOrDefault(s1.charAt(i), 0) + 1);
            map2.put(s2.charAt(i), map2.getOrDefault(s2.charAt(i), 0) + 1);
        }

        for (int i = n1; i < n2; i++) {
            if (map1.equals(map2))
                return true;

            char oldChar = s2.charAt(i - n1);
            map2.put(oldChar, map2.get(oldChar) - 1);
            System.out.println(map2);

            if (map2.get(oldChar) == 0)
                map2.remove(oldChar);

            char newChar = s2.charAt(i);
            map2.put(newChar, map2.getOrDefault(newChar, 0) + 1);
        }
        return map2.equals(map1);
    }
}