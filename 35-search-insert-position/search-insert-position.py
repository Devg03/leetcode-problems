class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count: int = 0
        numLen: int = len(nums)
        midLen: int = len(nums) // 2

        if target < nums[midLen]:
            for i in range(0, midLen):
                if nums[i] < target:
                    count += 1
        else:
            count += midLen
            for i in range(midLen, numLen):
                if nums[i] < target:
                    count += 1

        return count