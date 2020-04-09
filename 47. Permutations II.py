class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        used = [False for _ in range(0, len(nums))]

        def pu(path):
            # exit
            if len(path) == len(nums):
                ret.append(path[:])
                return
            for i in range(0, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    pu(path)
                    used[i] = False
                    path.pop()

        pu([])

        return ret


if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 2])
