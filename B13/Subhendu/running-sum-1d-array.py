class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ## https://leetcode.com/problems/running-sum-of-1d-array/

        sum_arr = [None] * len(nums)
        sum_arr[0] = nums[0]
        for i in range(1, len(nums)):
            sum_arr[i] = nums[i] + sum_arr[i-1]
        return sum_arr