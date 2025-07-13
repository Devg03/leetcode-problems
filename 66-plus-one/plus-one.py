class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigits = ""
        for i in digits:
            strDigits += str(i)

        intDigits = str(int(''.join(strDigits)) + 1)

        res = []
        for i in str(intDigits):
            res.append(int(''.join(i)))

        return res