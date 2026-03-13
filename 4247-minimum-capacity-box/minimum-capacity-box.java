class Solution {
    public int minimumIndex(int[] capacity, int itemSize) {
        int ans = -1;
        int prev = Integer.MAX_VALUE;

        for (int i = 0; i < capacity.length; i++) {
            if (capacity[i] >= itemSize && capacity[i] < prev) {
                ans = i;
                prev = capacity[i];
            }
        }

        return ans;
    }
}