class Solution:
    def __init__(self,s,t):
        self.s=s
        self.t=t
    def isSubsequence(self) -> bool:

         i, j = 0, 0

         while i < len(self.s) and j < len(self.t):
             if self.s[i] == self.t[j]:
                 i += 1
             j += 1

         return i == len(self.s) 


se="abc"
te="adhbty"
a=Solution(se,te)
print(a.isSubsequence())      