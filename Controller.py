import BoardModel, BoardView

class Controller:
    model = BoardModel.BoardModel()
    view = BoardView.BoardView()

    def __init__(self, model, view):
        self.model = model
        self.view = view


    def startSession(self):
        print("Session started!")