class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        left = curSum = maxSum = 0
        numSet = set()

        for right in range(len(nums)):
            while (right - left) + 1 > k or nums[right] in numSet:
                numSet.remove(nums[left])
                curSum -= nums[left]
                left += 1

            numSet.add(nums[right])
            curSum += nums[right]
            
            if (right - left) + 1 == k:
                maxSum = max(maxSum, curSum)

        return maxSum