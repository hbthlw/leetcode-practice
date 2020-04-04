# coding=utf-8
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def segment_valid(segment):
            if not segment:
                return False
            if segment[0] == '0':
                return len(segment) == 1
            else:
                return int(segment) <= 255

        segments = []
        output = []

        def back_track(pre_dot_position=-1, dots=3):
            # 递归出口
            if dots == 0:
                segment = s[pre_dot_position + 1:]
                if segment_valid(segment):
                    segments.append(segment)
                    output.append(".".join(segments))
                    segments.pop()
                return
            # 点的放置位置，只能隔1、2、3位
            for i in range(1, 4):
                segment = s[pre_dot_position + 1:pre_dot_position + 1 + i]

                if segment_valid(segment):
                    segments.append(segment)
                    back_track(pre_dot_position + i, dots - 1)
                    segments.pop()

        back_track()
        return output


if __name__ == '__main__':
    print Solution().restoreIpAddresses('1111')
