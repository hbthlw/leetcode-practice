# coding=utf-8
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
                # 因为排序了，所以每层相同元素，只取第一个
                # if i != start and candidates[i - 1] == candidates[i]:
                # 如果是本层的第一个，则它可以和之前的相同
                if i > start and candidates[i - 1] == candidates[i]:
                    continue

                path.append(candidates[i])
                search(i + 1, path)
                path.pop()

        search(0, [])

        return ret


if __name__ == '__main__':
    print Solution().combinationSum2([2, 5, 2, 1, 2], 5)
