class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums) + 1

        for i in range(0, n):
            if i not in sorted(nums):
                return i
            
        return 1