class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # declaring hashmap
        for i in range(len(nums)): # for loop to iterate through nums
            # Storing the complement/remaining number to reach target
            complement = target - nums[i]
            if complement in hashmap: # If complement in hashmap
                # return the complement and the current iteration num from nums
                return [i, hashmap[complement]] 
            # If not, 
            # add the current iteration of hashmap[i] = current iteration value of i
            hashmap[nums[i]] = i 

        return [] # If no matches are found return empty array
