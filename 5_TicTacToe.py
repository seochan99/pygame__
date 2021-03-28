#Tic Tac Toe
import random

def drawBoard(board):
    #이 함수는 파라미터로 받은 보드를 출력한다

    #board는 10개의 문자열로 된 리스트 이며 보드를 나타낸다(인덱스 0 은 무시)
    print("   |   |")
    print(" "+board[7]+" | "+board[8]+" | "+ board[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[4]+" | "+board[5]+" | "+ board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" "+board[1]+" | "+board[2]+" | "+ board[3])
    print("   |   |")

def inputPlayerLetter():
    #플레이어가 어떤 글자를 마크로 할 것인지를 선택하도록 한다.
    #플레이어가 선택한 글자를 첫 번째 아이템으로, 컴퓨터의 문자를 두 번쨰 아이템으로 하는 문자열을 반환한다.
    letter = " "
    while not(letter == "X" or letter == "O"):
        print("Do You Want to be X or O")
        letter = input().upper()

        #튜플의 첫 번째 요소가 플레이어의 글자이고 두 번째 요소는 컴퓨터의 글자다. 
        if letter =="X":
            return["X", "O"]
        else :
            return ["O","X"]

def whoGoseFirst():
    #누가 먼저 가 ? 
    if random.randint(0,1) == 0:
        return "Computer"
    else :
        return "Player"
        #like 동전던지기 ! 

def playAgain():
    #플레이어가 또 게임 한다고 하면 TRUE 안한다고하면  False
    print("Do you want to play again? (Yes or No)")
    return input().lower().startswith("n") #Y가 오면 True 반환 나머지는 False 

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo, le):
    # 보드와 플레이어의 글자를 주면, 플레이어가 이겼을 때 True를 반환한다.
    #Board 대신 Bo, Letter 대신 le를 써서 타이핑 하는 수고를 줄인다 . 굳이 ?
    return((bo[7]==le and bo[8]== le and bo[9]==le)) or ((bo[4]==le and bo[5]== le and bo[6]==le)) or ((bo[1]==le and bo[2]== le and bo[3]==le)) or ((bo[7]==le and bo[4]== le and bo[1]==le)) or ((bo[8]==le and bo[5]== le and bo[2]==le)) or ((bo[9]==le and bo[6]== le and bo[3]==le)) or ((bo[7]==le and bo[5]== le and bo[3]==le)) or((bo[9]==le and bo[5]== le and bo[1]==le))

def getBoardCopy(board):
    #  보드 리스트를 복제한 다음 복제한 리스트를 반환한다.
    dupeBoard = [] #인공지능은 원본 보드가 아니라 복사 보드에서  시뮬레이션을 해야하기에 만들어 줬다. 

    for i in board:
        dupeBoard.append(i) 
    
    return dupeBoard

def isSpaceFree(board,move):
    #보드에서 무브 위치가 비어 있으면 트투 반환
    return board[move]==" " # board[move] 가 비어 있으먄 True 를 반환한다 ! 

def getPlayerMove(board):
    #플레이어가 움직일 위치를 입력하도록 한다..
    move= " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board,int(move)):
        print("What is your next Move? (1-9)")
        move = input()
    return int(move) #input은 문자열이니깐 정수화 시켜 주즈아 ~~ 

def chooseRandomMoveFromList(board,moveList): #board는 틱택토 보드 의미. 무브리스트는 마크놓을 수 있는 위치 
    #movelist 와 board를 보고 가능한 위치를 반환한다.. 
    #가능한 윛가 하나도 없으면 None qksghksgksek,
    possibleMoves =[]
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board,computerLetter,playerLetter):
    #board, computerLetter를 보고, 컴퓨터의 차례에서 어디로 놓을지 결정한 다음 위치를 반환한다. 
    if computerLetter == "X":
        playerLetter =="O"
    else: 
        playerLetter="X"

    #틱택토 인공지능의 알고리즘
    #우선 다음에 이길 수 있는지 검사한다. 
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter, i)
            if isWinner(copy,computerLetter):
                return i 
    #상대편이 다음 번에 이길 수 있는지 검사해서 만약 그렇다면 막는다. 
    for i in range(1,10):
        copy = getBoardCopy(board) # 보드 짠 ! 
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i
    # 만약 비어 있으면 코너를 차지한다. 
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    #만약 비어 있으면 중앙을 차지한다
    if isSpaceFree(board,5):
        return 5

    #한쪽 면으로 이동한다.
    return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    #보드의 모든 공간이 다 찼으면 트루 아니면 폴스
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True 

##### main 시작 #####
print("Welcome To Tic Tac Toe!!")
print("---SPACE---")
print("   |   |")
print(" "+"7"+" | "+"8"+" | "+ "9")
print("   |   |")
print("-----------")
print("   |   |")
print(" "+"4"+" | "+"5"+" | "+ "6")
print("   |   |")
print("-----------")
print("   |   |")
print(" "+"1"+" | "+"2"+" | "+ "3")
print("   |   |")
while True:
    #보드 재설정
    theBoard=[" "]*10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoseFirst() # 턴 정하기 
    print("The " + turn + " will GO First !!")
    gameIsPlaying = True  # 이게 False 가 되면 game stop 

    while gameIsPlaying:
        if turn == "Player" : 
            #플레이어 차례
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray ! You have Won The Game")
                gameIsPlaying = False 
            else : 
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie ! ")
                    break
                else: 
                    turn = "Computer"

        else: # play computer 
            move = getComputerMove(theBoard,computerLetter,playerLetter)
            makeMove(theBoard,computerLetter,move)

            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print("The Computer Has Beaten You ! You Lose.!!")
                gameIsPlaying = False
            else : 
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie ! ")
                    break
                else: 
                    turn = "Player" 
    if playAgain():
        break


    #간단한 버그 수정 
    #칸을 좀 더 늘리고 싶음... 너무 칸이 좁음
    #인공지능 너무 똑똑... 절대 못이김.. 