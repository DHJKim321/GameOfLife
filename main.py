class Board:
    board = []


    def __init__(self, width: int=10, height: int=5):
        self.width = width
        self.height = height


    def initCells(self):
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                cell = Cell()
                row.append(cell)
            self.board.append(row)


    def printBoard(self):
        vertic_divider = "-" * (self.width + 2)
        horiz_divider = "|"
        print(vertic_divider)
        for i in range(self.height):
            curr_row = "|"
            for j in range(self.width):
                curr_row += self.board[i][j].draw()
            curr_row += "|"
            print(curr_row)
        print(vertic_divider)


    def returnLivingNeighbours(self, i, j):
        live_neighbours = 0
        for _i in range(i - 1, i + 2):
            for _j in range(j - 1, j + 2):
                if self.board[_i][_j].isAlive:
                    live_neighbours += 1
        return live_neighbours


class Cell:
    isAlive = False


    def draw(self):
        if not self.isAlive:
            return "."
        else:
            return "0"

    
    def killCell(self):
        if self.isAlive:
            self.isAlive = False

    
    def reviveCell(self):
        if not self.isAlive:
            self.isAlive = True


def main():
    brd = Board()
    brd.__init__()
    brd.initCells()
    brd.board[1][2].reviveCell()
    brd.board[2][2].reviveCell()
    brd.printBoard()
    print(brd.returnLivingNeighbours(1, 2))

main()