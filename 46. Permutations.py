class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False for _ in range(0, len(nums))]

        ret = []

        def permutation(path):
            if len(path) == len(nums):
                ret.append(path[:])

            for i in range(0, len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    permutation(path)

                    path.pop()
                    used[i] = False

        permutation([])
        return ret


if __name__ == '__main__':
    print Solution().permute([1, 2, 3])
