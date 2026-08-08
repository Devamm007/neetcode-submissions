class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = dict()
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in t:
            if char not in d or d[char] == 0:
                return False
            d[char] -= 1
        return True
            