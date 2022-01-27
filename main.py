import BoardView, Controller, BoardModel, InputUtil


def main():
    
    view = BoardView.BoardView()
    model = BoardModel.BoardModel()
    inputUtil = InputUtil.InputUtil()
    controller = Controller.Controller(model, view, inputUtil)
    controller.startSession()


main()