import BoardModel

class BoardView:


    def printBoard(self, width, height, board):
        vertic_divider = "-" * (width + 2)
        print(vertic_divider)
        for i in range(height ):
            curr_row = "|"
            for j in range(width):
                curr_row += board[i][j]
            curr_row += "|"
            print(curr_row)
        print(vertic_divider)