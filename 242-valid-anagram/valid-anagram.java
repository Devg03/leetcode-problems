class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] freqTable = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freqTable[s.charAt(i) - 'a']++;
            freqTable[t.charAt(i) - 'a']--;
        }
        for (int count = 0; count < 25; count++) {
            if (freqTable[count] != 0) return false;
        }

        return true;
    }
}