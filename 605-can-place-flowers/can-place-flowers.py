class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower = n
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if (flowerbed[i] == 0) and (flowerbed[i - 1] == 0) and (flowerbed[i+1] == 0):
                flowerbed[i] = 1                    
                if flower >= 1: 
                    flower -= 1

        return flower == 0