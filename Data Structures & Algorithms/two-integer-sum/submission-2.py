class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        visited = {}
        for i, num in enumerate(nums): # i is index
        # num is number
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            visited[num] = i