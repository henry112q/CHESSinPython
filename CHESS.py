class Main:
    def __init__(self):
        self.CurrentMove = None
        self.LastMove = None
        self.WhiteKingMove = False
        self.WhiteLRMove = False
        self.WhiteRRMove = False
        self.BlackKingMove = False
        self.BlackLRMove = False
        self.BlackRRMove = False
        self.RUNNING = True
        self.Turn = False
        self.FirstMoveInvalid = True
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
        self.FirstMoveInvalid = True
        while self.FirstMoveInvalid:
            self.FirstMove = input("Enter the coordinate of the piece that you want to move: ")
            if self.FirstMove.isalpha() == True:
                if self.FirstMove.upper() in ("Q","QUIT"):
                    self.FirstMoveInvalid = False
                    self.RUNNING = False
                    
            if len(self.FirstMove) != 2:
                continue
            
            if self.FirstMove.upper() in ("CK","CQ"):
                self.CastlingEvent = True
                self.FirstMoveInvalid = False if self.castlingValidation() else True
                string = "Castling with the seleceted side "+self.FirstMove.upper() if self.FirstMoveInvalid == False else ""
                
            
            if self.FirstMove[0].upper() not in ["A","B","C","D","E","F","G","H","C"] or self.FirstMove[1] not in ["1","2","3","4","5","6","7","8","K","Q"]:
                continue
            
            if self.FirstMove.upper() not in ("CK","CQ"):
            
                self.AlphaLocation = ord(self.FirstMove[0].upper())-65
                self.NumericalLocation = int(self.FirstMove[1])-1
                self.FirstPiece = self.PieceArray[self.NumericalLocation][self.AlphaLocation]
            
                if (self.FirstPiece[0] == "W" and self.Turn == True) or (self.FirstPiece[0] == "B" and self.Turn == False) or self.FirstPiece == "  ":
                    continue
                
                string = self.FirstPiece+" at postion "+self.FirstMove
            
            confirm = input("The piece you have selected is {} enter Y if correct and N if incorrect : ".format(string))
            if not confirm.isalpha() or len(confirm) != 1 :
                continue
            if confirm.upper() != "Y":
                continue
            
            self.FirstMoveInvalid = False
        
    
    def castlingValidation(self):
        
        Validate = False
        
        if self.FirstMove.upper() == "CK" :
            if self.WhiteKingMove == False and self.WhiteRRMove == False and self.Turn == False :
                Validate = True
                
            if self.WhiteKingMove == False and self.WhiteRRMove == False and self.Turn == True :
                Validate = True
                
        if self.FirstMove.upper() == "CQ" :
            if self.WhiteKingMove == False and self.WhiteLRMove == False and self.Turn == False :
                Validate = True
                
            if self.WhiteKingMove == False and self.WhiteLRMove == False and self.Turn == True :
                Validate = True
            
        if Validate == True:
            return True
        
        else:
            return False
    
         
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
            
if __name__ == "__main__":
    Running = Main()
    Running.Main()