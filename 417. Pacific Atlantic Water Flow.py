# coding=utf-8
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        pacific_ocean = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        atlantic_ocean = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # 上边连接太平洋 或 左边连接太平洋
                if i == 0 or j == 0:
                    self.dfs((i, j), matrix, pacific_ocean)
                # 下边连接大西洋 或 右边连接大西洋
                if i == len(matrix) - 1 or j == len(matrix[i]) - 1:
                    self.dfs((i, j), matrix, atlantic_ocean)

        ret = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if pacific_ocean[i][j] and atlantic_ocean[i][j]:
                    ret.append([i, j])
        return ret

    def dfs(self, point, matrix, ocean):
        ocean[point[0]][point[1]] = True
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for direction in directions:
            next_point = (point[0] + direction[0], point[1] + direction[1])
            if self.in_area(next_point, matrix) \
                    and matrix[next_point[0]][next_point[1]] >= matrix[point[0]][point[1]] \
                    and ocean[next_point[0]][next_point[1]] is False:
                self.dfs(next_point, matrix, ocean)

    def in_area(self, next_point, matrix):
        return -1 < next_point[0] < len(matrix) and -1 < next_point[1] < len(matrix[0])


if __name__ == '__main__':
    print Solution().pacificAtlantic([[3, 3, 3, 3, 3, 3],
                                      [3, 0, 3, 3, 0, 3],
                                      [3, 3, 3, 3, 3, 3]])
