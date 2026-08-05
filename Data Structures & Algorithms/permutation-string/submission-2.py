class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if m>n:
            return False

        target=[0]*26
        window=[0]*26

        for i in range(m):
            target[ord(s1[i])- 97]+=1
            window[ord(s2[i])- 97]+=1

        if window==target:
            return True

        for i in range(m,n):
            window[ord(s2[i])-97] +=1
            window[ord(s2[i - m])-97]-=1

            if window==target:
                return True
        return False


        