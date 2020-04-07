class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) > len(board) * len(board[0]):
            return False

        def in_area(point):
            return -1 < point[0] < len(board) and -1 < point[1] < len(board[0])

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def search(cr, word_index):

            if word_index == len(word) - 1:
                return word[word_index] == board[cr[0]][cr[1]]

            if board[cr[0]][cr[1]] == word[word_index]:
                visited[cr[0]][cr[1]] = True
                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

                for d in directions:
                    nr = (cr[0] + d[0], cr[1] + d[1])
                    if in_area(nr) and not visited[nr[0]][nr[1]] and search(nr, word_index + 1):
                        return True
                visited[cr[0]][cr[1]] = False
                return False

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0] and search((i, j), 0):
                    return True
        return False


if __name__ == '__main__':
    print Solution().exist([
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]],
        "ABCESEEEFS")
