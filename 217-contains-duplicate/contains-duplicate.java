class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int c = nums[i];
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }        

        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) > 1) {
                return true;
            }
        }
        return false;
    }
}