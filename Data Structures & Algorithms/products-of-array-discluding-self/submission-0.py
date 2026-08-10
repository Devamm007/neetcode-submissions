class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        output = []
        zero_count = 0 
        for num in nums:
            if num != 0:
                mul *= num
            else:
                zero_count += 1

        for num in nums:
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if num == 0:
                    output.append(mul)
                else:
                    output.append(0)
            else:
                output.append(mul//num)
        return output