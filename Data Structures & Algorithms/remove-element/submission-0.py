class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[-i-1] == val:
                nums.pop(-i-1)
                i -= 1
            i += 1

        return len(nums)