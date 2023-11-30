class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        newArr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                newArr.append("FizzBuzz")
            elif i % 3 == 0:
                newArr.append("Fizz")
            elif i % 5 == 0:
                newArr.append("Buzz")
            else:
                newArr.append(str(i))
        return newArr
    