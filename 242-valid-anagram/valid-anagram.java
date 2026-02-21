class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] freqTable = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freqTable[s.charAt(i) - 'a']++;
        }

        for (int j = 0; j < t.length(); j++) {
            freqTable[t.charAt(j) - 'a']--;
            if (freqTable[t.charAt(j) - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }
}