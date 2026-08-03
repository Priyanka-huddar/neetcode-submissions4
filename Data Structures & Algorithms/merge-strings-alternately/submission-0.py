class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        r=""
        while i<len(word1) or i<len(word2):
            if i<len(word1):
                r += word1[i]
            if i<len(word2):
                r += word2[i]
            i+=1
        return r
        