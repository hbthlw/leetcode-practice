class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]

        for i in range(0, len(nums)):
            temp_set = []
            for subset in ret:
                temp_set.append(subset + [nums[i]])
            ret.extend(temp_set)

        return ret


if __name__ == '__main__':
    print Solution().subsets([1, 2, 3])
