class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            value = nums.count(nums[i])
            if value == 1:
                return nums[i]
