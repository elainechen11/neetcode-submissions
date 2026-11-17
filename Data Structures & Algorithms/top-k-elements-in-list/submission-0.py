class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for item in nums:
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1
        arr = []
        for num, cnt in dic.items():
            arr.append([cnt, num])
        arr.sort()
        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result