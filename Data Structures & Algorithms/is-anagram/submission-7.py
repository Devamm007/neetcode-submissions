
class Solution:
    # similar to Counter from collections
    def counter(self, s: str) -> dict:
        d = dict()
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        # # method 1
        # if len(s) != len(t):
        #     return False
        # d = dict()
        # for char in s:
        #     if char in d:
        #         d[char] += 1
        #     else:
        #         d[char] = 1
        # for char in t:
        #     if char not in d or d[char] == 0:
        #         return False
        #     d[char] -= 1
        # return True

        if len(s) != len(t):
            return False

        return self.counter(s) == self.counter(t)
        
        
        
        
            