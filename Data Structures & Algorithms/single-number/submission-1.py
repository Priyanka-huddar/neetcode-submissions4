class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        for num in nums:
            i=num^i
        return i
        