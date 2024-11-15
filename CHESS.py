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
            
            self.moveInput = input("Enter the coordinate of the piece that you want to move: ")
            
            if self.moveInput.isalpha() == True and self.moveInput.upper() not in ("CQ","CK"): # Checks if the Input has a number and letter in it
                
                if self.moveInput.upper() in ("Q","QUIT"): # Checks if the user wants to end the game prematurely
                    self.FirstMoveInvalid = False
                    self.RUNNING = False
                    continue
                
                print("The Input Must contain a number the Required format is Letter A-H then Number 1-8 or CQ/CK")
                continue
                    
            if len(self.moveInput) != 2:
                print("Length of input is greater than two the Required format is Letter A-H then Number 1-8 or CQ/CK") # Checks for a Invalid Cooridnate
                continue
            
            if self.moveInput.upper() in ("CK","CQ"): # Checks for castling
                self.CastlingEvent = True
                self.FirstMoveInvalid = False if self.castlingValidation() else True
                string = "Castling with the seleceted side "+self.moveInput.upper() if self.FirstMoveInvalid == False else ""
                
            if self.moveInput[0].upper() not in ["A","B","C","D","E","F","G","H","C"] or self.moveInput[1] not in ["1","2","3","4","5","6","7","8","K","Q"]: # Checks that each charcter is a valid character at the right location
                continue
            
            if self.moveInput.upper() not in ("CK","CQ"): # Sorting out data for any other piece
            
                self.AlphaLocation = ord(self.moveInput[0].upper())-65
                self.NumericalLocation = int(self.moveInput[1])-1
                self.FirstPiece = self.PieceArray[self.NumericalLocation][self.AlphaLocation]
            
                if (self.FirstPiece[0] == "W" and self.Turn == True) or (self.FirstPiece[0] == "B" and self.Turn == False) or self.FirstPiece == "  ":
                    continue
                
                string = self.FirstPiece+" at postion "+self.moveInput
            
            confirm = input("The piece you have selected is {} enter Y if correct and N if incorrect : ".format(string))
            if not confirm.isalpha() or len(confirm) != 1 :
                continue
            if confirm.upper() != "Y":
                continue
            
            self.FirstMoveInvalid = False
        
    
    def castlingValidation(self):
        
        Validate = False
        
        if self.moveInput.upper() == "CK" :
            if self.WhiteKingMove == False and self.WhiteRRMove == False and self.Turn == False :
                Validate = True
                
            if self.WhiteKingMove == False and self.WhiteRRMove == False and self.Turn == True :
                Validate = True
                
        if self.moveInput.upper() == "CQ" :
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
            
            self.Turn = not self.Turn
            print(self.Turn)
            
if __name__ == "__main__":
    Running = Main()
    Running.Main()