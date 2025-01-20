class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid_point = len(nums) // 2

        return nums[mid_point]
        