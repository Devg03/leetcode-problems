class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    goodPairs += 1
        return goodPairs