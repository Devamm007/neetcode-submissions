class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = dict()
        # for num in nums:
        #     if num not in d:
        #         d[num] = 0
        #     d[num] += 1

        # for key in d.keys():
        #     if d[key] > len(nums) // 2:
        #         return key

        # return None 

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        freq = sum(1 for num in nums if num==candidate)
        if freq > len(nums) // 2:
            return candidate
        
        return None