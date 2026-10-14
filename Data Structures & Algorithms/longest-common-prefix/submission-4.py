class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        result = ''
        for i in range(n):
            prefix = strs[0][i]
            for str in strs:
                if i >= len(str):
                    return result
                if prefix != str[i]:
                    return result
            result += prefix 
        return result
        