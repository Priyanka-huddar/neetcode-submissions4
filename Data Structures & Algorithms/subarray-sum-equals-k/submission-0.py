class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        count=0
        prefix_sum=0
        for num in nums:
            prefix_sum+=num

            count+=freq.get(prefix_sum-k,0)

            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count
        