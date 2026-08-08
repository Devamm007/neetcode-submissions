class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # sorting algos are nlogn
        # # instead pass through and have counter
        # d = {0: 0, 1: 0, 2: 0}
        # for i in nums:
        #     d[i] += 1
        # for i in range(len(nums)):
        #     if i < d[0]:
        #         nums[i] = 0
        #     elif i < d[0] + d[1]:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2
        
        # one pass algo: dutch national flag algo
        low, mid, high = 0, 0, len(nums) - 1
        # low is end pointer to 0s (left to right)
        # mid is end pointer to 1s (left to right)
        # high is end pointer to 2s (right to left)

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1