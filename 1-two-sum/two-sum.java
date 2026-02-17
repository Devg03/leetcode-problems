class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> digits = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            digits.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (digits.containsKey(complement) && digits.get(complement) != i) {
                return new int[]{i, digits.get(complement)};
            }
        }
        return null;
    }  
}