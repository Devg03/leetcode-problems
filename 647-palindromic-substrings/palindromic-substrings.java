class Solution {
    public int countSubstrings(String s) {
        int palindromeCount = 0;
        int stringLength = s.length();

        for (int centerIndex = 0; centerIndex < stringLength * 2 - 1; centerIndex++) {
            int leftPointer = centerIndex / 2;
            int rightPointer = (centerIndex + 1) / 2;

            while ((leftPointer >= 0 && rightPointer < stringLength) && (s.charAt(leftPointer) == s.charAt(rightPointer))) {
                palindromeCount++;

                leftPointer--;
                rightPointer++;
            }
        }
        return palindromeCount;
    }
}