class InputUtil:


    def __init__(self):
        return

    
    def askToCustomiseBoard(self):
        answer = input("Would you like to customise your rows and columns?: (Y/N) ")
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            self.askToCustomiseBoard()


    def askForRows(self):
        return int(input("Enter number of rows: "))


    def askForCols(self):
        return int(input("Enter number of Columns: "))


    def askToSetCell(self):
        i = int(input("Enter row: "))
        j = int(input("Enter column: "))
        return [i, j]
