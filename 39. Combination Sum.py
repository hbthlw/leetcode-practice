class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []

        def search(start, path):

            if sum(path) > target:
                return

            if sum(path) == target:
                ret.append(path[:])
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                search(i, path)
                path.pop()

        search(0, [])

        return ret


if __name__ == '__main__':
    print Solution().combinationSum([2, 3, 6, 7], 7)
