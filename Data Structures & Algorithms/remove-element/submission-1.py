class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # # method 1
        # i = 0
        # while i < len(nums): # O(n)
        #     if nums[-i-1] == val:
        #         nums.pop(-i-1) # O(n)
        #         i -= 1
        #     i += 1

        # return len(nums)
        # # Above is O(n^2)

        # method 2
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i] = nums[-1]
                nums.pop()
            else:
                i += 1
        return len(nums)
        # similar logic but using pop() (pops last element which is O(1))
        # hence O(n)
