class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ret = []

        def search(start, path):
            if sum(path) == n and len(path) == k:
                ret.append(path[:])
                return

            if len(path) > k:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                search(i + 1, path)
                path.pop()
        search(0, [])

        return ret


if __name__ == '__main__':
    print Solution().combinationSum3(3, 7)
