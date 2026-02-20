class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxMult = 0;

        while (left < right) {
            maxMult = Math.max(Math.min(height[left], height[right]) * (right - left), maxMult);

            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return maxMult;
    }
}