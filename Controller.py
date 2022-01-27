import BoardModel, BoardView, InputUtil

class Controller:

    def __init__(self, model, view, inputUtil):
        self.model = model
        self.view = view
        self.inputUtil = inputUtil


    def startSession(self):
        print("Session started!")
        #customiseBoard = self.inputUtil.askToCustomiseBoard()
        self.model.initCells()
        self.view.printBoard(self.model.width, self.model.height, self.model.board)
        print(self.model.returnDeadNeighbours(0, 0))