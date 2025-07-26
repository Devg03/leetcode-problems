class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        elemCount = 1
        prevElem = nums[0]

        for i in range(len(nums)):
            if nums[i] != prevElem:
                elemCount += 1
                prevElem = nums[i]

            if elemCount == 3:
                return nums[i]

        return nums[0]