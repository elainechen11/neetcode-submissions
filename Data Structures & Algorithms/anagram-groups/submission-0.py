class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        temp = {}
        for word in strs:
            tup = tuple(sorted(word))
            if tup in temp:
                temp[tup].append(word)
            else:
                temp[tup] = [word]
        return list(temp.values())
        
        