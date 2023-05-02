class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in (0, 3, 6):
            for column in (0, 3, 6):
                val = self.isValidBox(board, row, column)
                if (val == False):
                    return False

        return (self.isValidRows(board) and self.isValidColumns(board))

    def isValidRows(self, board):
        for row in range(len(board)):
            rowSet = set()
            for column in range(len(board)):
                if board[row][column] == '.':
                    continue
                elif board[row][column] not in rowSet:
                    rowSet.add(board[row][column])
                else:
                    return False
        return True

    def isValidColumns(self, board):
        for column in range(len(board)):
            columnSet = set()
            for row in range(len(board)):
                if board[row][column] == '.':
                    continue
                elif board[row][column] not in columnSet:
                    columnSet.add(board[row][column])
                else:
                    return False
        return True

    def isValidBox(self, board, i, j):
        boxSet = set()
        for row in range(i, i + 3):
            for column in range(j, j + 3):
                if board[row][column] == '.':
                    continue
                elif board[row][column] not in boxSet:
                    boxSet.add(board[row][column])
                else:
                    return False
        return True