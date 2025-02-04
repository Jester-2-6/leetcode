class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_count = len(nums)

        for n1 in range(num_count - 1):
            for n2 in range (n1+1, num_count):
                if nums[n1] + nums[n2] == target:
                    return [n1, n2]



        return [n1, n2]
        