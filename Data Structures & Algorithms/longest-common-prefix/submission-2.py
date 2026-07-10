class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #n = len(strs)
        if len(strs)==0:
            return ""
        base = strs[0]
        result = ""
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i]!=base[i]:
                    #strs[j]
                    return result
            result+=base[i]
        return result
        