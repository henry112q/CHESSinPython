class Main:
    def __init__(self):
        
        #Move Validation
        self.CurrentMove = None
        self.LastMove = None
        self.WhiteKingMove = False
        self.WhiteLRMove = False
        self.WhiteRRMove = False
        self.BlackKingMove = False
        self.BlackLRMove = False
        self.BlackRRMove = False
        
        #ADMIN
        self.RUNNING = True
        self.Turn = False
        
        #Move Logic
        self.FirstMoveInvalid = True
        self.moveInput = None
        self.Piece = None
        self.SecondMoveInvalid = True
        self.destinationInput = None
        self.moveInvalid = True
        self.changedInitialSelection = False
        
        #Display vars
        self.PieceArray = [["WR","WN","WB","WQ","WK","WB","WK","WR"],
                           ["WP","WP","WP","WP","WP","WP","WP","WP"],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["  ","  ","  ","  ","  ","  ","  ","  "],
                           ["BP","BP","BP","BP","BP","BP","BP","BP"],
                           ["BR","BK","BB","BQ","BK","BB","BK","BR"]]
        self.CHESSBOARD = " \n   ---A-----B-----C-----D-----E-----F-----G-----H---\n 8 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 7 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 6 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 5 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 4 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 3 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 2 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | ------------------------------------------------- \n 1 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|\n   ------------------------------------------------- \n"
    
    def FirstMoveInput(self):
        
        self.FirstMoveInvalid = True
        
        while self.FirstMoveInvalid:
            
            self.moveInput = input("Enter the coordinate of the piece that you want to move: ")
            
            if self.moveInput.isalpha() == True and self.moveInput.upper() not in ("CQ","CK"): # Checks if the Input has a number and letter in it
                
                if self.moveInput.upper() in ("Q","QUIT"): # Checks if the user wants to end the game prematurely
                    self.FirstMoveInvalid = False
                    return
                
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
                print("The format of your input is incorrect please use the Required format which is Letter A-H then Number 1-8 or CQ/CK")
                continue
            
            if self.moveInput.upper() not in ("CK","CQ"): # Sorting out data for any other piece
            
                self.AlphaLocation = ord(self.moveInput[0].upper())-65 # Gets location of piece on the array
                self.NumericalLocation = int(self.moveInput[1])-1
                self.Piece = self.PieceArray[self.NumericalLocation][self.AlphaLocation]
            
                if (self.Piece[0] == "W" and self.Turn == True) or (self.Piece[0] == "B" and self.Turn == False) or self.Piece == "  ": 
                    print("The location you have selected is blank or the opponents piece")
                    continue
                
                string = self.Piece+" at postion "+self.moveInput
            
            confirm = input("The piece you have selected is {} enter Y if correct and N if incorrect : ".format(string))
        
            if not confirm.isalpha() or len(confirm) != 1 :
                continue
        
            if confirm.upper() != "Y":
                continue
            
            self.FirstMoveInvalid = False
    
    def SecondMoveInput(self):
        self.SecondMoveInvalid = True
        
        if self.moveInput.upper() in ("CK",'CQ'): # checks for castling as it dose not need this section
            return
        
        while self.SecondMoveInput:
            
            self.destinationInput = input("please enter where you want the piece to go on the board: ")
            
            if self.destinationInput.upper() in ('Q','QUIT'): # checks for a quit command 
                self.RUNNING = False
                return
            
            if self.destinationInput.upper() in ('Z','U','UNDO'):
                self.changedInitialSelection = True   
                return
            
            
    
    def castlingValidation(self):
        
        Validate = False
        
        if self.moveInput.upper() == "CK" :
        
            if self.WhiteKingMove == False and self.WhiteRRMove == False and self.Turn == False :
                Validate = True
                
            if self.BlackKingMove == False and self.BlackRRMove == False and self.Turn == True :
                Validate = True
                
        if self.moveInput.upper() == "CQ" :
        
            if self.WhiteKingMove == False and self.WhiteLRMove == False and self.Turn == False :
                Validate = True
                
            if self.BlackKingMove == False and self.BlackLRMove == False and self.Turn == True :
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
            self.moveInput = True
            
            while self.moveInvalid: # Gets the move and makes sure it can be repeated if there is a mistake
                
                self.FirstMoveInput()

                if self.RUNNING == False: 
                    self.moveInvalid = False

                    continue

                self.SecondMoveInput()

                if self.RUNNING == False: 
                    self.moveInvalid = False
                    continue
                
                if self.changedInitialSelection == True: # Restarts the Cycle if there is a mistake
                    self.changedInitialSelection == False
                    print("Restarting your go")
                    continue
                
            self.Turn = not self.Turn
            print(self.Turn)
            
if __name__ == "__main__":
    Running = Main()
    Running.Main()