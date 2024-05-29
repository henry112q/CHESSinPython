class Main:
    def __init__(self):
        self.CurrentMove = None
        self.LastMove = None
        self.WhiteCheck = None
        self.BlackCheck = None
        self.RUNNING = True
        self.Turn = False
        self.PieceArray = [["WR","WN","WB","WQ","WK","WB","WK","WR"],
                           ["WP","WP","WP","WP","WP","WP","WP","WP"],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["BP","BP","BP","BP","BP","BP","BP","BP"],
                           ["BR","BK","BB","BQ","BK","BB","BK","BR"]]
        self.CHESSBOARD = " \n   ---A-----B-----C-----D-----E-----F-----G-----H---\n 8 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 7 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 6 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 5 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 4 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 3 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 2 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | ------------------------------------------------- \n 1 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|\n   ------------------------------------------------- \n"
    def MoveInputs(self):
        FirstMoveInvalid = True
        while FirstMoveInvalid:
            self.FirstMove = input("Enter the coordinate of the piece that you want to move: ")
            if len(self.FirstMove) != 2:
                continue
            if self.FirstMove[0].upper() not in ["A","B","C","D","E","F","G","H"] or self.FirstMove[1] not in ["1","2","3","4","5","6","7","8"]:
                continue
            self.AlphaLocation = ord(self.FirstMove[0].upper())-65
            self.NumericalLocation = int(self.FirstMove[1])-1
            self.FirstSquare = self.PieceArray[self.NumericalLocation][self.AlphaLocation]
            print(self.FirstSquare)
            
    def DisplayBoard(self):
        pieces = []
        unchangedArray = self.PieceArray
        unchangedArray.reverse()
        for Array in unchangedArray:
            for item in Array:
                pieces.append(item)
        print(self.CHESSBOARD.format(*pieces))
        self.PieceArray.reverse()
        
    def Main(self):
        while self.RUNNING:
            self.DisplayBoard()
            self.MoveInputs()
            self.RUNNING = False
            
if __name__ == "__main__":
    Running = Main()
    Running.Main()