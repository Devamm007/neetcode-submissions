class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # # O(n^2)

        visited = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return [visited[complement], i]
            visited[num] = i
