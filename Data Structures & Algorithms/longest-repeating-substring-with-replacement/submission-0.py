class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        mapp={}
        max_length=0
        maxFreq=0
        while r<len(s):
            if s[r] not in mapp:
                mapp[s[r]]=1
            else:
                mapp[s[r]]+=1
            maxFreq=max(maxFreq,mapp[s[r]])
            while (r-l+1)-maxFreq>k:
                mapp[s[l]]-=1
                if mapp[s[l]]==0:
                    del mapp[s[l]]
                l+=1
            max_length=max(max_length,r-l+1)
            r+=1
        return max_length
        