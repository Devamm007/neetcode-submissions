class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        # 1,2,3,4
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        # 1,1,2,6

        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        # 24,12,8,6

        return output

        # mul = 1
        # output = []
        # zero_count = 0 
        # for num in nums:
        #     if num != 0:
        #         mul *= num
        #     else:
        #         zero_count += 1

        # for num in nums:
        #     if zero_count > 1:
        #         return [0 for _ in range(len(nums))]
        #     elif zero_count == 1:
        #         if num == 0:
        #             output.append(mul)
        #         else:
        #             output.append(0)
        #     else:
        #         output.append(mul//num)
        # return output