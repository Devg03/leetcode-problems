class Solution:
    def removeDuplicates(self, numbers: List[int]) -> int:
        i = 1
        
        for j in range(1, len(numbers)):
            if numbers[i - 1] != numbers[j]:
                numbers[i] = numbers[j]
                i += 1

        return i