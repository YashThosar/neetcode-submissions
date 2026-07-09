class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        original_target = target
        for i in range(n):
            complement = original_target - nums[i]
            if complement in nums and nums.index(complement)!=i:
                return sorted([i, nums.index(complement)])
               # return indices