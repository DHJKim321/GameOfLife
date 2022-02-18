class BoardModel:
    board = []
    new_live_cells = []
    new_dead_cells = []


    def __init__(self, width: int=10, height: int=5):
        self.width = width
        self.height = height


    def setWidthAndHeight(self, width, height):
        self.__init__(width, height)


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


    def getCell(self, i, j):
        return self.board[i][j]


    def addNewLivingCell(self, i, j):
        self.new_live_cells.append((i, j))


    def getNewLivingCells(self):
        return self.new_live_cells
    

    def addNewDeadCell(self, i, j):
        self.new_dead_cells.append((i, j))


    def getNewDeadCells(self):
        return self.new_dead_cells

    
    def returnLivingNeighbours(self, i, j):
        live_neighbours = 0
        for _i in range(i - 1, i + 2):
            if _i >= 0 and _i < self.height:
                for _j in range(j - 1, j + 2):
                    if (_j >= 0 and _j < self.width) and self.getCell(_i, _j) == "0" and [i, j] != [_i, _j]:
                        live_neighbours += 1
        return live_neighbours


    def returnDeadNeighbours(self, i, j):
        dead_neighbours = 0
        for _i in range(i - 1, i + 2):
            if _i >= 0 and _i < self.height:
                for _j in range(j - 1, j + 2):
                    if (_j >= 0 and _j < self.width) and self.getCell(_i, _j) == "." and [i, j] != [_i, _j]:
                        dead_neighbours += 1
        return dead_neighbours


    def checkUnderPopulation(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.returnLivingNeighbours(i, j) < 2:
                    self.killCell(i, j)

    
    def isBoardEmpty(self):
        for row in self.board:
            if row.count("0") != 0:
                return False
        return True