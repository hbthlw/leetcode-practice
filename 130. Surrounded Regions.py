class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1:
                    if board[i][j] == 'O':
                        self.bfs_region(board, i, j)
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'

    def bfs_region(self, board, i, j):
        queue = [(i, j)]
        visited = set()
        while queue:
            region = queue[0]
            queue = queue[1:]
            board[region[0]][region[1]] = 'T'
            for adjacent in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_i, next_j = region[0] + adjacent[0], region[1] + adjacent[1]
                if -1 < next_i < len(board) and -1 < next_j < len(board[next_i]) and board[next_i][next_j] == 'O':
                    if (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))
                        queue.append((next_i, next_j))


if __name__ == '__main__':
    board = [["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X"],
             ["O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O"],
             ["O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
             ["X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O"],
             ["O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O"],
             ["X", "O", "O", "O", "X", "X", "X", "O", "X", "O", "O", "O", "O", "X", "X", "O", "X", "O", "O", "O"],
             ["O", "O", "O", "O", "O", "X", "X", "X", "X", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O"],
             ["X", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "X", "X", "O", "O", "X", "O", "O", "X"],
             ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "O", "O", "X", "O", "X"],
             ["O", "O", "O", "O", "X", "O", "X", "O", "O", "X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O"],
             ["X", "X", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "X", "O", "O", "O", "X", "O", "X", "O", "O", "O", "X", "O", "X", "O", "X", "O", "O"],
             ["O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O", "X", "O"],
             ["X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "X", "X", "O", "O", "O", "X", "O", "O"],
             ["O", "O", "X", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "X", "O", "X", "O", "X", "O", "O"],
             ["O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "X", "X", "O", "O", "X", "O", "O", "O", "X", "O"],
             ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
             ["X", "O", "O", "O", "O", "X", "O", "O", "O", "X", "X", "O", "O", "X", "O", "X", "O", "X", "O", "O"]]
    Solution().solve(board)

    print board
