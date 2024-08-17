class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        while count < 31:
            if (2 ** count) == n:
                return True
            else:
                count += 1

        return False