class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0
        n1, n2 = len(word1), len(word2)
        n = min(n1, n2)
        result = ""
        while left < n:
            result += word1[left]
            result += word2[right]
            left += 1
            right += 1
        if n1 < n2:
            result += word2[right:]
        elif n2 < n1:
            result += word1[left:]
        return  result
            

        