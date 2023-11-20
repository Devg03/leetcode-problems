class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in accounts:
            for j in i:
                if sum(i) > maxWealth:
                    maxWealth = sum(i)
        return maxWealth