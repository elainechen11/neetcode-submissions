class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)
        nums1 = nums[:-1]
        nums2 = nums[1:]
        for i in range(n-2, -1, -1):
            dp1[i] = max(dp1[i+2]+nums1[i], dp1[i+1])
            dp2[i] = max(dp2[i+2]+nums2[i], dp2[i+1])
        return max(dp1[0], dp2[0])



        