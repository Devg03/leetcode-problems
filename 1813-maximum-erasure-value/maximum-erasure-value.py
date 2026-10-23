class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        uniqueNum = set()
        left = curSum = maxSum = 0

        for right in range(len(nums)):
            while nums[right] in uniqueNum:
                uniqueNum.remove(nums[left])
                curSum -= nums[left]
                left += 1

            uniqueNum.add(nums[right])
            curSum += nums[right]

            maxSum = max(maxSum, curSum)
        
        return maxSum