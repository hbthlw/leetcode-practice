class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []

        def process(path, start):
            ret.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                process(path, i + 1)
                path.pop()

        process([], 0)

        return ret


if __name__ == '__main__':
    print Solution().subsetsWithDup([1, 2, 2])
