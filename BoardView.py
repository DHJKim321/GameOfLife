class BoardView:

    
    def printBoard(self):
        vertic_divider = "-" * (self.width + 2)
        print(vertic_divider)
        for i in range(self.height):
            curr_row = "|"
            for j in range(self.width):
                curr_row += self.board[i][j].draw()
            curr_row += "|"
            print(curr_row)
        print(vertic_divider)