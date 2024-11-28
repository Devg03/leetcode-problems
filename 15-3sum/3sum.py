class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []

        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]

            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                if k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                
                jkSum = nums[j] + nums[k]
                if jkSum == target:
                    solution.append([nums[i], nums[j], nums[k]])
                
                if jkSum > target:
                    k -= 1
                else:
                    j += 1

            i += 1
        
        return solution