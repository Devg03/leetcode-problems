class Solution:
    def calPoints(self, operations: List[str]) -> int:
        perform = []
        for i in operations:
            if i != "C" and i != "D" and i != "+":
                perform.append(int(i))
            elif i == "C":
                perform.remove(perform[-1])
            elif i == "D":
                perform.append(2 * int(perform[-1]))
            elif i == "+":
                add = (int(perform[len(perform) - 2])) + int(perform[len(perform) - 1])
                perform.append(add)

        return sum(perform)
