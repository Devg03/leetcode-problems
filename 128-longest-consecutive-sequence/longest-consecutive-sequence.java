class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Set<Integer> numbers = new HashSet<Integer>();
        for (int i : nums) {
            numbers.add(i);
        }

        int longestStreak = 0;
        for (int i : numbers) {
            if (!numbers.contains(i - 1)) {
                int currentNum = i;
                int currentStreak = 1;

                while (numbers.contains(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}