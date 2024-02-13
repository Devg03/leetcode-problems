class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        counter = 0
        newList = []

        for i in nums:
            counter = 0
            for j in nums:
                if (j < i):
                    counter += 1
            newList.append(counter)


        return newList