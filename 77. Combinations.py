class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        used = [False for _ in range(0, n + 1)]
        ret = []

        def do_combination(start=1, stack=[]):
            if len(stack) == k:
                ret.append(stack[:])
                return
            for i in range(start, n + 1):
                if not used[i]:
                    used[i] = True
                    stack.append(i)
                    do_combination(i + 1, stack)
                    used[i] = False
                    stack.pop()

        do_combination()
        return ret


if __name__ == '__main__':
    print Solution().combine(4, 2)
