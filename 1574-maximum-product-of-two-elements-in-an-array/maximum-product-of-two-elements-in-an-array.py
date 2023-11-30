class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mxProduct = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if ((nums[i]-1) * (nums[j]-1)) > mxProduct:
                    mxProduct = (nums[i]-1) * (nums[j]-1)

        return mxProduct