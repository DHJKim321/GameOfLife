class BoardModel:
    board = []


    def __init__(self, width: int=10, height: int=5):
        self.width = width
        self.height = height


    def initCells(self):
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(".")
            self.board.append(row)

    
    def reviveCell(self, i, j):
        self.board[i][j] = "0"


    def killCell(self, i, j):
        self.board[i][j] = "."

    
    def returnLivingNeighbours(self, i, j):
        live_neighbours = 0
        for _i in range(i - 1, i + 2):
            if _i >= 0 and _i < self.height:
                for _j in range(j - 1, j + 2):
                    if self.board[_i][_j] == "0" and (_j >= 0 and _j < self.width):
                        live_neighbours += 1
        if live_neighbours == 0:
            return 0
        else:
            return live_neighbours - 1


    def returnDeadNeighbours(self, i, j):
        dead_neighbours = 0
        for _i in range(i - 1, i + 2):
            if _i >= 0 and _i < self.height:
                for _j in range(j - 1, j + 2):
                    if self.board[_i][_j] == "." and (_j >= 0 and _j < self.width):
                        dead_neighbours += 1
        return dead_neighbours - 1