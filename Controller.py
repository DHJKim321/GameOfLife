class Controller:

    def __init__(self, model, view, inputUtil):
        self.model = model
        self.view = view
        self.inputUtil = inputUtil


    def startSession(self):
        print("Session started")
        print("Welcome to the Game of Life!")
        customiseBoard = self.inputUtil.askToCustomiseBoard()
        if customiseBoard:
            row = self.inputUtil.askForRows()
            col = self.inputUtil.askForCols()
            self.model.setWidthAndHeight(col, row)
        self.model.initCells()
        self.view.printBoard(self.model.width, self.model.height, self.model.board)
        setMore = "y"
        while setMore.lower() == "y":
            cell = self.inputUtil.askToSetCell()
            i = cell[0]
            j = cell[1]
            self.model.reviveCell(i, j)
            setMore = self.inputUtil.setMoreCells()
        self.view.printBoard(self.model.width, self.model.height, self.model.board)
        while not self.model.isBoardEmpty():
            self.model.checkUnderPopulation()
            self.model.checkOverPopulation()
            self.view.printBoard(self.model.width, self.model.height, self.model.board)
        

    