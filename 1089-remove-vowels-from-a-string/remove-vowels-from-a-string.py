class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        listS = list(s)

        for i in s:
            if i in vowels:
                listS.remove(i)

        return "".join(listS)
