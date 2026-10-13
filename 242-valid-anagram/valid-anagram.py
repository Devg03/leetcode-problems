class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for i in s:
            if i in counter:
                counter[i] += 1
            else:    
                counter[i] = 1


        print(counter)
        for i in t:
            if (i not in counter) or (t.count(i) != counter[i]):
                return False

        return True