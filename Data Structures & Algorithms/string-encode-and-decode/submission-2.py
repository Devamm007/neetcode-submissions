class Solution:
    # # Length Prefic Encoding Method
    # def __init__(self):
    #     # can be any character other than 0-9 digits
    #     self.delimiter = ' '

    # def encode(self, strs: List[str]) -> str:
    #     encoded = []
    #     for s in strs:
    #         encoded.append(f"{len(s)}{self.delimiter}{s}")
    #     return "".join(encoded)

    # def decode(self, s: str) -> List[str]:
    #     strs = []
    #     i = 0
    #     while i < len(s):
    #         j = i
    #         while s[j] != self.delimiter:
    #             j+=1

    #         length = int(s[i:j])

    #         i = j+1
    #         strs.append(s[i:i+length])

    #         i += length
    #     return strs

    # Escaping Method
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            escaped_s = s.replace('\\', '\\\\').replace(',', '\\,')
            encoded.append(escaped_s)
        return ','.join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strs = []
        current = []
        i = 0
        while i < len(s):
            # escape
            if s[i] == '\\' and i+1 < len(s):
                current.append(s[i+1])
                i+=2
            # end
            elif s[i] == ',':
                strs.append("".join(current))
                current = []
                i+=1
            # continue
            else:
                current.append(s[i])
                i+=1
        # last word
        strs.append("".join(current))
        return strs