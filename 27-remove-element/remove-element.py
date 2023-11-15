class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while count < len(nums):
            if nums[count] == val:
                nums.pop(count)
                count -= 1
            count += 1
        return len(nums)
