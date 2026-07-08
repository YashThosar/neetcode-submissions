class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        my_dict = {}

        if len(s)!=len(t):
            return False
        for i in s:
            my_dict[i]=my_dict.get(i,0)+1
        for s in t:
            if s in my_dict and my_dict[s]>0:
                my_dict[s]-=1
            else:
                return False
        return True
