class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        for i in range(0, len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    pairs += 1
        return pairs
    