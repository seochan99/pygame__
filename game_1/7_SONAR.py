#Sonar 

import random
import sys 
import math 

#### Function #### 
def getNewBoard():
    #새 60 *15 보드 데이터 구조를 만든다.
    board = []
    for x in range(60): #메인 리스트는 60개의 리스트로 된 리스트이다. 
        board.append([]) #60개의 빈리스트 추가   // [[y좌표]*60이라는 말씀 ! ]
        for y in range(15): #메인 리스트의 각 리스트는 15개의 문자열이 있다. 
            #읽기 쉽도록 바다에는 다른 문자를 사용한다 ! 
            if random.randint(0,1) == 0 : # ' 중  랜덤으로 출력해서 바다를 그려준다 ! 
                board[x].append("~")
            else : 
                board[x].append("`")
    return board 
    # 즉, board[0]은 []이므로 ! 여기에 ~'이거를 15개 더한다 ! 이렇게 새로줄을 총 60개를 만든다 ! 에에 
def getRandomChests(numChests): #보물상자의 위치를 결정 ! 
    #보물상자 데이터 구조를 리스트로 만든다.(보물상자는 x,y 좌표로 된 리스트이다 ! ).
    chests=[]
    while len(chests) <numChests:
        newChests = [random.randint(0,59), random.randint(0,14)] 
        if newChests not in chests: 
            chests.append(newChests) 
    return chests

def drawBoard(board):
    #보드 데이터 구조를 화면상에 그린다. 
    hline = '    '#보드의 왼쪽애 ㅅ나오는 숫자 앞에 보이는 공간
    for i in range(1,6): #1,2,3,4,5 를 그리는거다 ! 
        hline+=(' '*9)+str(i)
    #윗부분에 숫자를 찍는다.
    print(hline)
    print('   ' +("0123456789"*6)) #실제코드에서 12345143123213 하면 실수하니 이르케 곱셈으로 하면 편함 ! 
    print()
    #각각 15줄을 출력한다. 
    for i in range(15):
        # 한 자리 숫자면 앞쪽에 빈칸 하나를 채워 자릿수를 맞춰야 한다. 
        if i<10 :
            extraSpace = "  "
        else:
            extraSpace = " "

        #바다에서 가로 행의 상태 만들기 
        boardRow = ""
        for column in range(60):
            boardRow+=board[column][i]
        print("%s%s %s %s"%(extraSpace, i, boardRow,i)) # y축 그리는중 -- 9 바다바다바답다받답다받 9 이런식임 ! 
        #아랫부분에 숫자를 찍는다. 
    print()
    print('   ' + ('0123456789' * 6))
    print(hline)

def isValidMove(x,y):
    #보드의 좌표이면 트루 아니면 폴스
    return x>=0 and x<=59 and y>=0 and y<= 14

def makeMove(board,chests,x,y):
    #보드 데이터 구조를 응파탐지기 문자가 있는 것으로 바꾼다. 
    # #보물상자를 찾으면 chests 리스트에서 제거한다.
    # 적절하지 않은 움직임이면 False 적절하면 움직인 결과에 대한 문자열을 반환한다. 
    if not isValidMove(x,y):
        return False 
    
    smallestDistance = 100 #모든 보물 상자는 거리 100안에 위치한다.
    for cx,cy in chests: #for 문을 돌리면서 각 보물상자와 탐지기와의 거리중에서 가장 가까운 보물상자의 위치만을 알려준다 ! 
        #chests 가 [5,0],[3,5]]를가지면 처음에는 5,0을 두번째에서는 3,5를 반환한다 ! 
        if abs(cx - x) > abs(cy - y): #절댓값 엑스좌표가 더 크면 엑스좌표 반환 
            distance = abs(cx-x)
        else:
            distance = abs(cy - y) #보드는 네모네모 픽셀로 되었으니 x,y중에서 더 가까운 값을 플레이어에게 알려준다 ! 

        if distance<smallestDistance: #가장 가까운 보물상자를 찾는다 ! 
            smallestDistance = distance

    if smallestDistance == 0:
        #여기가 바로 보물상자 위치다 !!!!!
        chests.remove([x,y])
        return "You Have Found a sunken Treasure Chest!"
    else:
        if smallestDistance<10: #10아래 거리를 알려준다 ! 
            board[x][y] = str(smallestDistance)
            return "Treasure detected at a distance of %s form the sonar device. "%(smallestDistance)
        else:
            board[x][y] = " O "
            return "Sonar did not detect anything. All Treasure chests out of range" #10보다 더 먼거리에 떨어뜨렸을때는 암것도 안알려준다 ! 


def enterPlayerMove():
    #플레이어가 위치를 입력하도록 한다. x,y좌표로 된 리스트를 반환한다.
    print("where do you want to drop the next sonar device? (X : 0-59 | Y : 0-14 )(or The Quit)")
    while True:
        move = input() #어디갈지 입력 받는다 ! 
        if move.lower() =="quit":
            print("Thanks For Playing This Game! Have Good Day!")
            sys.exit() # sys 모듈의 끝내기 !!!

        move = move.split() #띄어쓰기 기준으로 X Y좌표를 분간한다 ! 아직 문자열이기때문에 밑에서 int를 쳐주는 것이다. -> 문자열 move[0]= x move[1] = Y이다 ! 
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]),int(move[1])] # 이 까다로운 조건을 만족시키면 리턴해서 이 함수를 탈출한다 isdigit->모두 숫자로 구성되어있으면 True를 반환한다!
        print("Enter A number From 0 to 59, a space, then a number from 0 to 14.")  #탈출하지 못한다면 이 멘트를 출력한다 ! 

def playAgain():
    print("Do you want to play Again?(Y/N)")
    return input().lower().startswith("y")

# def showInstructions():
#     print('''Instructions: You are the captain of the Simon, a treasure-hunting ship. Your current mission is to use sonar devices to find three sunken treasure chests at the bottom of\
# the ocean. But you only have cheap sonar that finds distance, not direction.

# Enter the coordinates to drop a sonar device. The ocean map will be marked with
# how far away the nearest chest is, or an X if it is beyond the sonar device's
# range. For example, the C marks are where chests are. The sonar device shows a
# 3 because the closest chest is 3 spaces away.

# 1 2 3
# 012345678901234567890123456789012

# 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
# 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
# 2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
# 3 ````````~~~`````~~~`~`````~`~``~` 3
# 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

# 012345678901234567890123456789012
# 1 2 3
# (In the real game, the chests are not visible in the ocean.)

# Press enter to continue...''')
#     input()

#     print('''When you drop a sonar device directly on a chest, you retrieve it and the other
# sonar devices update to show how far away the next nearest chest is. The chests
# are beyond the range of the sonar device on the left, so it shows an X.

# 1 2 3
# 012345678901234567890123456789012

# 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
# 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
# 2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
# 3 ````````~~~`````~~~`~`````~`~``~` 3
# 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

# 012345678901234567890123456789012
# 1 2 3

# The treasure chests don't move around. Sonar devices can detect treasure chests
# up to a distance of 9 spaces. Try to collect all 3 chests before running out of
# sonar devices. Good luck!

# Press enter to continue...''')
#     input() 내일... 

##### Main ##### 
print("S O N A R ! ")
print()
print("Would you like to view the instructions? (Y/N)")
# if input.().lower().startswith("y"):
#     showInstructions()
input("go start?")
while True:
    #r게임 설정 
    sonarDevices = 16
    theBoard = getNewBoard() #이를 통해서 바다를 만든다  ! 
    theChests = getRandomChests(3) #보물 3개 ! 
    drawBoard(theBoard) #보드를 그려봅시당 ~ 
    previousMoves=[]

    while sonarDevices >0: #아직 기회가 있다 ! 
        #차례를 시작한다. 
        
        #음파탐지기/보물상자 상태
        if sonarDevices>1: extraSsonar = "s" #1개 초과한 갯수를 개지고 있으면 s를 붙여줘야한다 ! device -> devices 
        else: extraSsonar= " "
        if len(theChests)>1: extraSchest ="s"
        else: extraSchest=" "
        print("you have %s sonar device %s left. %s treasure chests %s remain-ing."%(sonarDevices, extraSsonar, len(theChests),extraSchest))

        x,y = enterPlayerMove() #x,y 입력받은 좌표를 가져온다 
        previousMoves.append([x,y]) # previousMouse 리스트에 삽입 ! 

        moveResult = makeMove(theBoard,theChests,x,y)
        if moveResult ==False:
            continue 
        else:
            if moveResult == "You have Found a Sunken Treasure Chest! ":
                #현재 지도상의 모든 음파탐지기를 갱신한다.
                for x,y in previousMoves:
                    makeMove(theBoard,theChests,x,y)
            drawBoard(theBoard)
            print(moveResult)
        
        if len(theChests) ==0:
            print("You have found all the sunken treasure chests! Congratulations and good Game!")
            break
        sonarDevices -= 1

    if sonarDevices==0:
        print("We\"ve run out of sonar devices! Now we have to Turn the Ship around and head")
        print("for home with Treasure chests still out there ! GAME OVER ! ")
        print("    The Remaining Chests were here :")
        for x,y in theChests:
            print("    %s, %s" %(x,y))

    if not playAgain():
        sys.exit()