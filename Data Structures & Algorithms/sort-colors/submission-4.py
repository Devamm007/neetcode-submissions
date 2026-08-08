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

"""
Conceptual Overview: Extending Dutch National Flag (DNF) to k-Way Partitioning
================================================================================

Why DNF Works for k = 3 in 1 Pass & O(1) Space:
- Arrays only have two physical ends (Index 0 and Index N-1).
- Pointers moving inward from both ends (low & high) define 3 implicit zones:
  1. [0 ... low-1]      -> Category 0
  2. [low ... high]     -> Category 1 (the squeezed middle)
  3. [high+1 ... N-1]   -> Category 2

Why k-Way Partitioning (k > 3) Fails the "1 Pass + O(1) Space" Rule:
- With k > 3, there are more than 3 target regions, but an array still only 
  has 2 physical ends to swap elements toward.
- You cannot track and maintain k-1 in-place boundaries simultaneously in 
  a single directional scan without overlapping intermediate sub-ranges.

The Fundamental Trade-off for k > 3:

Option A) Maintain O(1) Auxiliary Space (Multi-Pass Partitioning / Multi-Pivot Quicksort)
  - Process: Recursively or iteratively apply 2-way/3-way partitions to sub-arrays.
  - Time Complexity:  O(N log k)
  - Space Complexity: O(1) extra space (or O(log k) recursion stack)
  - Pass Count:       ~log2(k) passes over the data

Option B) Maintain a Single Pass (Counting Sort / Bucket Sort)
  - Process: Scan elements once, using dynamic pointers/counts for all k categories.
  - Time Complexity:  O(N + k)
  - Space Complexity: O(k) extra space for dynamic bucket pointers or frequency counts
  - Pass Count:       1 pass (or 2 passes for counting + overwrite)
"""