import BoardView, Controller, BoardModel


def main():
    
    view = BoardView.BoardView()
    model = BoardModel.BoardModel()
    controller = Controller.Controller(model, view)
    controller.startSession()

main()