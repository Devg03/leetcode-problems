class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * (len(nums))
        right = [0] * (len(nums))

        answer = []
        for i in range(1, len(nums)):
            left[0] = 1
            left[i] = left[i - 1] * nums[i - 1]

        for j in reversed(range(len(nums) - 1)):
            right[len(nums) - 1] = 1
            right[j] = right[j + 1] * nums[j + 1]
        
        for k in range(len(nums)):
            answer.append(left[k] * right[k])

        return answer
