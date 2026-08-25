class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen=set(nums)
        for number in range(1,len(nums) + 2):
            if number not in seen:
                return number
        