class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        min=n//3
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        result=[]
        for key,value in d.items():
            if value>min:
                result.append(key)
        return result