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

    # # Escaping Method
    # def encode(self, strs: List[str]) -> str:
    #     if not strs:
    #         return "EMPTY"
    #     encoded = []
    #     for s in strs:
    #         escaped_s = s.replace('\\', '\\\\').replace(',', '\\,')
    #         encoded.append(escaped_s)
    #     return 'LIST,'+','.join(encoded)

    # def decode(self, s: str) -> List[str]:
    #     if s == 'EMPTY':
    #         return []
    #     else:
    #         s = s[5:]
    #     strs = []
    #     current = []
    #     i = 0
    #     while i < len(s):
    #         # escape
    #         if s[i] == '\\' and i+1 < len(s):
    #             current.append(s[i+1])
    #             i+=2
    #         # end
    #         elif s[i] == ',':
    #             strs.append("".join(current))
    #             current = []
    #             i+=1
    #         # continue
    #         else:
    #             current.append(s[i])
    #             i+=1
    #     # last word
    #     strs.append("".join(current))
    #     return strs

    # Chunked Transfer Encoding
    def __init__(self):
        self.chunksize = 4
        self.delimiter = '#'

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY"
        encoded = []
        for s in strs:
            for i in range(0, len(s), self.chunksize):
                chunk = s[i : i + self.chunksize]
                encoded.append(f"{len(chunk)}{self.delimiter}{chunk}")
            encoded.append(f"0{self.delimiter}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == 'EMPTY':
            return []
        strs = []
        current_str = []
        i = 0
        while i < len(s):
            j = s.find(f'{self.delimiter}', i)
            length = int(s[i:j])

            if length == 0:
                strs.append("".join(current_str))
                current_str = []
                i = j+1
            else:
                i = j+1
                current_str.append(s[i:i+length])
                i += length

            # length = 0
            # while s[i] != f'{self.delimiter}':
            #     length = length * 10 + int(s[i])
            #     i += 1
            # i+=1

            # if length == 0:
            #     strs.append("".join(current_str))
            #     current_str = []
            # else:
            #     current_str.append(s[i:i+length])
            #     i += length

        return strs