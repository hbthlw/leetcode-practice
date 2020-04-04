class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if not digits:
            return []
        pads = [[],
                [],
                ['a', 'b', 'c'],
                ['d', 'e', 'f'],
                ['g', 'h', 'i'],
                ['j', 'k', 'l'],
                ['m', 'n', 'o'],
                ['p', 'r', 'q', 's'],
                ['t', 'u', 'v'],
                ['w', 'x', 'y', 'z']]

        def back_tracking(cur_letters, next_digits):
            if len(next_digits) == 0:
                ret.append(cur_letters)
                return
            letters = pads[int(next_digits[0])]
            for letter in letters:
                back_tracking(cur_letters + letter, next_digits[1:])

        back_tracking('', digits)
        return ret


if __name__ == '__main__':
    print Solution().letterCombinations('23')
