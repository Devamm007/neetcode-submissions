class Solution:
    def __init__(self):
        # can be any character other than 0-9 digits
        self.delimiter = ' '

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}{self.delimiter}{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != self.delimiter:
                j+=1

            length = int(s[i:j])

            i = j+1
            strs.append(s[i:i+length])

            i += length
        return strs

