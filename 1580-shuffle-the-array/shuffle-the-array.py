class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
            newArr = []
            result = []
            for i in range(n, len(nums)):
                newArr.append(nums[i])

            for i in range(0, n):
                result.append(nums[i])
                result.append(newArr[i])

            return (result)