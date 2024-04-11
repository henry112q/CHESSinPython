#FUNCTIONS

def DisplayBoard(A8,B8,C8,D8,E8,F8,G8,H8,
                 A7,B7,C7,D7,E7,F7,G7,H7,
                 A6,B6,C6,D6,E6,F6,G6,H6,
                 A5,B5,C5,D5,E5,F5,G5,H5,
                 A4,B4,C4,D4,E4,F4,G4,H4,
                 A3,B3,C3,D3,E3,F3,G3,H3,
                 A2,B2,C2,D2,E2,F2,G2,H2,
                 A1,B1,C1,D1,E1,F1,G1,H1,
                 chessBoard):
    print(chessBoard.format(
                            A8,B8,C8,D8,E8,F8,G8,H8,
                            A7,B7,C7,D7,E7,F7,G7,H7,
                            A6,B6,C6,D6,E6,F6,G6,H6,
                            A5,B5,C5,D5,E5,F5,G5,H5,
                            A4,B4,C4,D4,E4,F4,G4,H4,
                            A3,B3,C3,D3,E3,F3,G3,H3,
                            A2,B2,C2,D2,E2,F2,G2,H2,
                            A1,B1,C1,D1,E1,F1,G1,H1))

def StartValidation(turn,WKM,BKM,A1,B1,C1,D1,E1,F1,G1,H1,A8,B8,C8,D8,E8,F8,G8,H8,WR1M,WR2M,BR1M,BR2M):
    while True:
        
        startSquare = input("Choose the coordinates of the piece you which to move: ").upper()
        
        if startSquare in ("A1","A2","A3","A4","A5","A6","A7","A8",
                           "B1","B2","B3","B4","B5","B6","B7","B8",
                           "C1","C2","C3","C4","C5","C6","C7","C8",
                           "D1","D2","D3","D4","D5","D6","D7","D8",
                           "E1","E2","E3","E4","E5","E6","E7","E8",
                           "F1","F2","F3","F4","F5","F6","F7","F8",
                           "G1","G2","G3","G4","G5","G6","G7","G8",
                           "H1","H2","H3","H4","H5","H6","H7","H8",
                           "CK","CQ"):
            
            if startSquare in ("CK","CQ"):
                colour = turn % 2
                
                if colour == 0:
                    
                    if startSquare == "CK":
                        if F1 == " " and G1 == " " and WKM == 0 and WR2M == 0:
                            return ("Castle","WK")
                        else:
                            print("Castle could not be completed due to one of two reasons \nF1 and G1 are not empty or King or Knight has already moved")
                    
                    else:
                        if B1 == " " and C1 == " " and D1 == " " and WKM == 0 and WR1M == 0:
                            return ("Castle","WQ")
                        else:
                            print("Castle could not be completed due to one of two reasons \nB1 C1 and D1 are not empty or King or Knight has already moved")
                
                if colour == 1:
                    
                    if startSquare == "CK":
                        if F8 == " " and G8 == " " and BKM == 0 and BR2M == 0:
                            return ("Castle","BK")
                        else:
                            print("Castle could not be completed due to one of two reasons \nF8 and G8 are not empty or King or Knight has already moved")
                    
                    else:
                        if B8 == " " and C8 == " " and D8 == " " and BKM == 0 and BR1M == 0:
                            return ("Castle","BQ")
                        else:
                            print("Castle could not be completed due to one of two reasons \nB8 C8 and D8 are not empty or King or Knight has already moved")
            else:
                
                if globals()[startSquare] == " ":
                    print("No piece at this Coordnate")
                else:
                    colour = turn%2
                    
                    if colour == 0 and globals()[startSquare][0] == "W":
                        if globals()[startSquare]=="WK":
                            WKM += 1
                        elif startSquare=="A1":
                            WR1M += 1
                        elif startSquare == "H1":
                            WR2M += 1
                        break
                    
                    elif colour == 1 and globals()[startSquare][0] == "B":
                        if globals()[startSquare]=="BK":
                            BKM += 1
                        elif startSquare=="A8":
                            BR1M += 1
                        elif startSquare=="H8":
                            BR2M += 1
                        break
                    else:
                        print("Piece is not yours")
        else:
            print("Coordnate dose not exist")
    return startSquare

def EndValidation():
    while True:
        endSquare = input("Choose the coordinates of the location you want to move to: ").upper()
        if endSquare in ("A1","A2","A3","A4","A5","A6","A7","A8",
                         "B1","B2","B3","B4","B5","B6","B7","B8",
                         "C1","C2","C3","C4","C5","C6","C7","C8",
                         "D1","D2","D3","D4","D5","D6","D7","D8",
                         "E1","E2","E3","E4","E5","E6","E7","E8",
                         "F1","F2","F3","F4","F5","F6","F7","F8",
                         "G1","G2","G3","G4","G5","G6","G7","G8",
                         "H1","H2","H3","H4","H5","H6","H7","H8"):
            break
    return endSquare

#VARIABLES

chessBoard = " \n   ---A-----B-----C-----D-----E-----F-----G-----H---\n 8 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 7 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 6 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 5 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 4 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 3 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | -------------------------------------------------\n 2 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}| \n | ------------------------------------------------- \n 1 |{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|{:^5}|\n   -------------------------------------------------"

WKM = 0
BKM = 0
WR1M = 0
WR2M = 0
BR1M = 0
BR2M = 0


BLA = " "
BP1 = "BP"
BP2 = "BP"
BP3 = "BP"
BP4 = "BP"
BP5 = "BP"
BP6 = "BP"
BP7 = "BP"
BP8 = "BP"

WP1 = "WP"
WP2 = "WP"
WP3 = "WP"
WP4 = "WP"
WP5 = "WP"
WP6 = "WP"
WP7 = "WP"
WP8 = "WP"

BK = "BK"
BQ = "BQ"
BR1 = "BR"
BR2 = "BR"
BN1 = "BN"
BN2 = "BN"
BB1 = "BB"
BB2 = "BB"

WK = "WK"
WQ = "WQ"
WR1 = "WR"
WR2 = "WR"
WN1 = "WN"
WN2 = "WN"
WB1 = "WB"
WB2 = "WB"

A8 = BR1
B8 = BN1
C8 = BB1
D8 = BQ
E8 = BK
F8 = BB2
G8 = BN2
H8 = BR2

A7 = BP1
B7 = BP2
C7 = BP3
D7 = BP4
E7 = BP5
F7 = BP6
G7 = BP7
H7 = BP8

A6 = BLA
B6 = BLA
C6 = BLA
D6 = BLA
E6 = BLA
F6 = BLA
G6 = BLA
H6 = BLA

A5 = BLA
B5 = BLA
C5 = BLA
D5 = BLA
E5 = BLA
F5 = BLA
G5 = BLA
H5 = BLA

A4 = BLA
B4 = BLA
C4 = BLA
D4 = BLA
E4 = BLA
F4 = BLA
G4 = BLA
H4 = BLA

A3 = BLA
B3 = BLA
C3 = BLA
D3 = BLA
E3 = BLA
F3 = BLA
G3 = BLA
H3 = BLA

A2 = WP1
B2 = WP2
C2 = WP3
D2 = WP4
E2 = WP5
F2 = WP6
G2 = WP7
H2 = WP8


A1 = WR1
B1 = WN1
C1 = WB1
D1 = WQ
E1 = WK
F1 = WB2
G1 = WN2
H1 = WR2

turn = 0

#MAIN

while True:
    DisplayBoard(A8,B8,C8,D8,E8,F8,G8,H8,
                 A7,B7,C7,D7,E7,F7,G7,G7,
                 A6,B6,C6,D6,E6,F6,G6,H6,
                 A5,B5,C5,D5,E5,F5,G5,H5,
                 A4,B4,C4,D4,E4,F4,G4,H4,
                 A3,B3,C3,D3,E3,F3,G3,H3,
                 A2,B2,G2,D2,E2,F2,G2,H2,
                 A1,B1,C1,D1,E1,F1,G1,H1,
                 chessBoard)
    startsquare = StartValidation(turn,WKM,BKM,A1,B1,C1,D1,E1,F1,G1,H1,BLA,WR2,WK,WR1M,WR2M,BR1M,BR2M)
    if startsquare[0] != "Castle":
        
        if globals()[startsquare][-1] == "P":
            typeOfPiece = "P"
        elif globals()[startsquare][-1] == "R":
            typeOfPiece = "R"
        elif globals()[startsquare][-1] == "N":
            typeOfPiece = "N"
        elif globals()[startsquare][-1] == "B":
            typeOfPiece = "B"
        elif globals()[startsquare][-1] == "K":
            typeOfPiece = "K"
        elif globals()[startsquare][-1] == "Q":
            typeOfPiece = "Q" 
        
        endsquare = EndValidation()
        piece = globals()[startsquare]
        globals()[startsquare] = BLA
        globals()[endsquare] = piece
        
    else:
        castletype = startsquare[1]
         
        if castletype == "WK":
            G1 = WK
            F1 = WR2
            E1 = BLA
            H1 = BLA
            
        elif castletype == "WQ": 
            B1 = WK
            C1 = WR1
            E1 = BLA
            A1 = BLA
        
        elif castletype == "BK": 
            G8 = BK
            F8 = BR2
            E8 = BLA
            H8 = BLA
        
        elif castletype == "BQ": 
            B8 = BK
            C8 = BR1
            E8 = BLA
            A8 = BLA
    
    turn += 1
