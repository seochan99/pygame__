#Reversi

import random
import sys 
### function ###

def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')#end를 써서 줄바꿈이 안일어나게 한다. 
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)

def resetBoard(board):
    #넘겨받은 보드를 원래의 시작위치를 제외하고 깨끗하게 리셋한다.
    for x in range(8):
        for y in range(8):
            board[x][y] = " "

    #시작위치
    board[3][3] = "X"
    board[3][4] = "O"
    board[4][3] = "O"
    board[4][4] = "X" #게임을 시작할때 각 플레이어는 중앙에 타일을 두 장씩 깔고 시작해야 한다 ! 

def getNewBoard():
    #비어 있는 새 board 데이터 구조를 만든다.
    board=[]
    for i in range(8):
        board.append([" "]*8)
    return board 
    #board는 8개의 리스트로 된 리스트이며 각8개리스트는 8개의 문자열을 가지고 있다. ex(board[0]=[[][][][][]...]) 이것이 8개 ! 

def isOnBoard(x,y):
    #보드에 좌표 있으면 트루 
    return x>=0 and x<=7 and y>=0 and y<=7

def isValidMove(board,tile,xstart,ystart):
    #플레이어가 놓은 위치인 x , y 가 적절한 위치가 아니면 False 
    #만약 적절한 위치면 플레이어가 놓은 위치에 따라 플레이어의 타일이 된 영역을 모두 리스트로 만들어서 반환한다. 
    if board[xstart][ystart] != " "or not isOnBoard(xstart,ystart):
        return False

    board[xstart][ystart] = tile #임시로 보드에 타일을 놓는다. 
    if tile == "X":
        otherTile = "O"
    else:
        otherTile = "X"
    
    tileToFlip =[]
    for xdirection,ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        x,y = xstart,ystart
        x += xdirection #해당 방향으로 첫 번째 스텝을 이동해본다.
        y += ydirection 
        if isOnBoard(x,y) and board[x][y] == otherTile:
            # 내 타일 옆에 상대편의 타일이 있는 경우 
            x += xdirection
            y += ydirection
            if not isOnBoard(x,y):
                continue
            while board[x][y] == otherTile:
                x+= xdirection
                y+= ydirection
                if not isOnBoard(x,y): #while뮨울 빠져나온다음 for 문에서 컨티뉴로 진행한다 
                    break
            if not isOnBoard(x,y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break 
                    tileToFlip.append([x,y])
    board[xstart][ystart] = " " # 빈 공간으로 되돌린다.
    if len(tileToFlip)==0:
        return False#만약 뒤집히는 타일이 없으면 유효한 위치가 아니다. 
    return tileToFlip

def getBoardCopy(board):
    #보드의 복사본을 만들어서 복사본을 반환한다. 
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y] #board복사   

def getBoardWithValidMoves(board,tile):
    #플레이어가 놓을 수 있는 유효한 위치에 "."" 을 표시해서 새 board를 반환한다.
    dupeBoard = getBoardCopy(board)

    for x,y in getValidMoves(dupeBoard,tile):
        dupeBoard[x][y] = "." #dupe보드에 . 그려주기 
    return dupeBoard

def getValidMoves(board,tile):
    #주어진 보드에서 플레이어가 놓을 수 있는 유효한 위치로 된 리스트를[x,y]로 반환한다. 
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board,tile,x,y) != False:
                validMoves.append([x,y])
    return validMoves

def getScoreOfBoard(board):
    #타일을 새서 점수를 계산한다. 키 X O로된 딕셔너리를 반환한다. 
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] =="X":
                xscore+=1
            if board[x][y] == "O":
                oscore+=1
    return{"X":xscore, "O":oscore}

def enterPlayerTile():
    #플레이어가 어떤 타일로 게임을 할 것인지를 선택하도록 한다,
    #플레이어의 타일을 첫 번째 아이템으로, 컴퓨터의 타일으 ㄹ두 번쨔 아이템으로 하는 리스트를 반환한다 ! 
    tile = " "
    while not(tile=="X" or tile =="O"):
        print("Do You want to be X or O ?")
        tile = input().upper()

    # 튜플의 첫 번째 요소는 플레이어 타일이고, 두 번째 요소는 컴퓨터의 타일이다. 
    if tile == "X":
        return ["X","O"] #플레이어 X
    else:
        return ["O","X"] #player O 

def whoGoseFirst():
    #누가 먼저 플레이 할 것인지 임의로 정한다. 
    if random.randint(0,1) == 0 :
        return "computer"
    else:
        return "plyaer" 
        #0이 나오면 컴퓨터부터 아니면 플레이어 부터 

def playAgain():
    # 플레이어가 또 게임을 하겠다고 하면 ㅇㅇ 아니면 ㄴㄴ
    print("Do you want to play agian?(yes or no)")
    return input().lower().startswith("y")

def makeMove(board, tile, xstart, ystart):
    # 보드에 에긋 와이 위치에 타일을 놓은 다음 상대편의 타일을 뒤집는다.
    #유효하지 않은 위치라면 False 를 반환하고 그렇지 않으면 트루를 반환한다
    tilesToFlip = isValidMove(board,tile,xstart,ystart)
    if tilesToFlip == False:
        return False
    
    board[xstart][ystart] = tile
    for x,y in tilesToFlip:
        board[x][y] = tile
    return True 

def isOnCorner(x,y):
    # 1 corner return True 
    return (x==0 and y==0) or (x==7 and y==0) or (x==0 and y==7) or (x==7 and y==7)

def getPlayerMove(baord,playerTile):
    #플레이어에게 위치를 입력하도록 한다. 
    #위치를 [x,y]로 반환한다 (아니면 힌트나 쿼잇 문자열을 반환한다.)
    DIGITS1TO8 = "1 2 3 4 5 6 7 8".split()
    while True:
        print("Enter your move, or type quit to end the game, or hints to turn off/on hunts.")
        move = input().lower()
        if move=="quit":
            return "quit"
        if move=="hints":
            return "hints"
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) -1
            y = int(move[0]) -1 
            if isValidMove(board,playerTile,x,y) == False :
                continue
            else:
                break 
        else:
            print("That is not a valid move. type the x digit (1-8), then the y digit (1-8)")
            print("For example, 81 will be the top- right corner ! ")

def getComputerMove(board, computerTile):
    #board와 computerTile을 받아 어디에 놓을 것인지 결정한 다음,
    #위치를 [x,y] 리스트로 반환한다.
    possibleMoves =getValidMoves(board,computerTile)

    #가능한 위치의 순서를 임의로 정한다. 
    random.shuffle(possibleMoves)

    #만약 가능하다면 코너를 차지한다
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return[x,y]
    #가능한 모든 위치에 대해 검사한 다음 가장 높은 점수를 얻을 수 있는 위치를 기엉ㄱ한다. 
    bestScore = -1
    for x,y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard,computerTile,x,y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score>bestScore:
            bestMove =[x,y]
            bestScore = score
    return bestMove


def showPoints(playerTile,computerTile):
    #현재 점수를 출력한다
    scores = getScoreOfBoard(mainBoard)
    print("YOu have %s points. The Computer has %s points."%(scores[playerTile],scores[computerTile]))

### main ###

print(" Welcome to Reversi!")
while True:
    #보드와 게임을 리셋한다
    mainBoard = getNewBoard() #빈칸 만들기 
    resetBoard(mainBoard) 
    playerTile, computerTile = enterPlayerTile() #첫번째로는 플레이어의 타일 두번째로는 컴퓨터의 타일을 받는다.
    showHints = False #힌트는 우선 가리기 
    turn = whoGoseFirst()
    print(f"First Play is {turn} ! ")

    while True:
        if turn == "player":
            #플레이어의 차례
            if showHints: #힌트 보여주는 보드 그리기 .. 
                validMovesBoard = getBoardWithValidMoves(mainBoard,playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile,computerTile)
            move = getPlayerMove(baord,playerTile)
            if move =="quit":
                print("Thanks For Playing !")
                sys.exit()
            elif move =="hints":
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard,playerTile,move[0],move[1])
            if getValidMoves(mainBoard,computerTile) == []:
                break
            else:
                turn = "computer"
        else:#computer
            drawBoard(mainBoard)
            showPoints(playerTile,computerTile)
            input("Press Enter To see the Computer\"s move.")
            x,y = getComputerMove(mainBoard,computerTile)
            makeMove(mainBoard,computerTile,x,y)

            if getValidMoves(mainBoard,playerTile)==[]:
                break
            else:
                turn = "player"

        #최종 점수를 표시한다.
        drawBoard(mainBoard)
        scores = getScoreOfBoard(mainBoard)
        print("X scored %s points. O scored %s points." %(scores["X"],scores["O"]))
        if scores[playerTile]>scores[computerTile]:
            print("You Beat The computer by %s points ! Congratulations!"%(scores[playerTile]-scores[computerTile]))
        elif scores[playerTile] < scores[computerTile]:
            print("Yout lost. the computer beat you by %s points."%(scores[computerTile]-scores[playerTile]))
        else:
            print("The Game was a tie ! ")
        
        if not playAgain():
            break
                
