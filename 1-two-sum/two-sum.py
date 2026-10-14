class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        table = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in table:
                return [table[complement], i]

            table[nums[i]] = i
