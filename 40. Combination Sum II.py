class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        print candidates

        def search(start, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                ret.append(path[:])
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i - 1] == candidates[i]:
                    continue

                path.append(candidates[i])
                search(i + 1, path)
                path.pop()

        search(0, [])

        return ret


if __name__ == '__main__':
    print Solution().combinationSum2([2, 5, 2, 1, 2], 5)
