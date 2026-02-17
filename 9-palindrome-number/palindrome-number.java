class Solution {
    public boolean isPalindrome(int x) {
        List<Character> numList = new ArrayList<>();

        for (char c : String.valueOf(x).toCharArray()) {
            numList.add(c);
        }

        for (int i = 0; i < numList.size() - 1; i++) {
            if (!Objects.equals(numList.get(i), numList.get(numList.size() - i - 1))) {
                return false;
            }
        }

        return true;
    }
}