class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        for key in d.keys():
            if d[key] > len(nums) // 2:
                return key
                
        return None 