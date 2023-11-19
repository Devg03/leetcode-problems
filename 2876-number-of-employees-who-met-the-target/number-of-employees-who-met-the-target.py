class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        numEmployees = 0
        for i in hours:
            if i >= target:
                numEmployees += 1

        return numEmployees
    