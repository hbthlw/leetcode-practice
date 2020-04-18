class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []

        def is_palindrome(s):
            return s == s[::-1]

        def do_partition(string, path):

            if not string:
                ret.append(path[:])
                return

            for i in range(0, len(string)):
                if is_palindrome(string[0:i + 1]):
                    path.append(string[0:i + 1])
                    do_partition(string[i + 1:], path)
                    path.pop()

        do_partition(s, [])

        return ret


if __name__ == '__main__':
    print Solution().partition("aab")
