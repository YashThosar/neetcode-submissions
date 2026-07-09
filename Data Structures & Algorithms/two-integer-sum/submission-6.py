class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        my_dict = {}
        for i in range(n):
            my_dict[nums[i]]=i
        for j in range(n):
            complement = target - nums[j]
            if complement in my_dict and my_dict[complement]!=j:
                return [j,my_dict[complement]]  