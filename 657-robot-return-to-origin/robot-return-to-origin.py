class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countV = 0
        countH = 0

        for move in moves:
            if move == "U":
                countV += 1
            elif move == "D":
                countV -= 1
            elif move == "L":
                countH -= 1
            elif move == "R":
                countH += 1
        
        return True if countV == 0 and countH == 0 else False