class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        while count < len(nums):
            if nums.count(nums[count]) > 1:
                nums.pop(count)
                count -= 1
            count += 1
        return len(nums)
