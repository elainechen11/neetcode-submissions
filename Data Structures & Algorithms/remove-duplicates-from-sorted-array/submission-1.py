class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                nums.pop(slow)
            else:
                fast += 1
                slow += 1
        return len(nums)
