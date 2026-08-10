class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = {0: 1}
        count = 0
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum - k in prefix_sum:
                count += prefix_sum[curr_sum-k]
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = 0
            prefix_sum[curr_sum] += 1
        return count
        