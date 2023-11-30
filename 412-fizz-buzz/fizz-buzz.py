class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        newArr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                newArr.insert(len(newArr), "FizzBuzz")
            elif i % 3 == 0:
                newArr.insert(len(newArr), "Fizz")
            elif i % 5 == 0:
                newArr.insert(len(newArr), "Buzz")
            else:
                newArr.insert(len(newArr), str(i))

        return newArr

       