class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None for _ in range(0, len(nums))]
        max_sub = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_sub = max(max_sub, dp[i])
        return max_sub


if __name__ == '__main__':
    print Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
