class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        # We set the rows and cols variables to the length of dungeon(rows) and columns of dungeon(cols)
        rows, cols = len(dungeon), len(dungeon[0])
        # We set every block to infinity value as we are trying the determine the next best step (previous last step)
        dp = [[float("inf")] * cols for _ in range(rows)]
        
        def get_min_health(currCell:int, nextRow:int, nextCol: int) -> float:
            # If the nextRow or nextCol is out of bounds, simply return infinity
            if nextRow >= rows or nextCol >= cols:
                return float("inf")
            
            # Next cell to move set in nextCell var
            nextCell = dp[nextRow][nextCol]

            # We compare 1 (default health) with the cost in health if we were to move to the next cell
            return max(1, nextCell - currCell)

        # We are iterating in reverse as we are going from bottom right to top left
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                # currentCell is the last cell of the dungeon as we are going in reverse
                currCell = dungeon[row][col]

                # calculate min health needed if the knight were to move rightwards
                right_health = get_min_health(currCell, row, col + 1)
                # calculate min health needed if the knight were to move downwards
                down_health = get_min_health(currCell, row + 1, col)

                # Make decision based on which gives a lesser value
                next_health = min(right_health, down_health)

                # If the next_health isn't infinity
                if next_health != float("inf"):
                    # next_health is the min_health
                    min_health = next_health
                else:
                    # If the current cell is empty, then it can't hurt you hence min_health = 1
                    if currCell >= 0:
                        min_health = 1
                    # if the knight encounters a demon, subtract health
                    else:
                        min_health = 1 - currCell
                
                # Each cell we go to we store the knight's min health required at that cell
                dp[row][col] = min_health

        return dp[0][0] # Returns the min health required at the last cell in other words the starting point