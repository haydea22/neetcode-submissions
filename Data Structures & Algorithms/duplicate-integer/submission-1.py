class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i, num in enumerate(nums):
            if num in h:
                return True
            h[num] = i
        return False