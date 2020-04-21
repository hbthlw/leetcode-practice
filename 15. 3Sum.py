class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                if nums[i] + (nums[lo] + nums[hi]) == 0:
                    ret.append([nums[i], nums[lo], nums[hi]])
                    lo = lo + 1
                    hi = hi - 1
                    while lo < len(nums) and nums[lo] == nums[lo - 1]:
                        lo = lo + 1
                    while hi > lo and nums[hi] == nums[hi + 1]:
                        hi = hi - 1
                elif nums[i] + (nums[lo] + nums[hi]) < 0:
                    lo = lo + 1
                else:
                    hi = hi - 1

        return ret


if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
