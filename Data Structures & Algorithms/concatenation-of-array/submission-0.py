class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        nums2 = []
        for i in range(n):
            nums2.append(nums[i])
        ans = nums+nums2
        return ans
        