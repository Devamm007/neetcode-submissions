class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''

        # vertical scanning
        prefix = strs[0]
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != prefix[i]:
                    return prefix[:i]
        return prefix

        # sorting
        # strs.sort() # in-place
        # # strs = sorted(strs) # not in-place
        # prefix = ''
        # for i in range(min(len(strs[0]), len(strs[-1]))):
        #     if not strs[0][i] == strs[-1][i]:
        #         return prefix
        #     prefix += strs[0][i]

        # # horizontal scanning
        # prefix = strs[0]
        # for s in strs[1:]:
        #     while not s.startswith(prefix):
        #         prefix = prefix[:-1]
        #         if not prefix:
        #             return ''
        # return prefix
        # # O(s) S is sum of length of all words
        # # O(1) space complexity
