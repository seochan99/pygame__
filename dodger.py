#### 모듈가져오기 ####
import pygame, random, sys
from pygame.locals import *
 #key dwon같은거 가지고이씀 

#### 상수 정의 ####
WINDOWWIDTH = 600
WINDOWHEIGHT =600
TEXTCOLOR =(255,255,255)
BACKGROUNDCOLOR=(0,0,0)
#상수로 정의함으로서 언제든지 ~ 편하게 수정가능하다 ! 
FPS = 40
#mainClock.tick(FPS) 초당프레임 수
#악당을 설명하는 상수 
BADDIEMINSIZE = 10 #악당너비
BADDIEMAXSIZE = 40 #악당 높이이 사이가 될것 
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8 #속도도 이 사이가 될것 
ADDNEWBADDIEMRATE = 6 # 이만큼의 반복문을 돌 때마다 악당 추가요 ~ 
PLAYERMOVERATE = 5 #플레이어 속도 

#### 함수 정의 ####
def terminate():
    pygame.quit()
    sys.exit() #end game 

#wait player     
def waitForPlayerToPressKey(): 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate() #나가는지 확인 
            if event.type == KEYDOWN : #키를 눌렀냐 ~?
                if event.key == K_ESCAPE: #눌렀는데 esc누른거면 ㅃㅇ
                    terminate() 
                return #아니면 반환하고 함수 ㅃㅇ~ 

#악당과 플레이어가 겹치는지 확인하는 함수 
def playerHitBAddie(playerRect,baddies):
    for b in baddies: #baddies 모든 악당 
        if playerRect.colliderect(b['rect']): #모든 악당의 각 크기와 위치 값 전달 
            return True #collidrect는 둘이 겹치면 트루 아니면 폴스 
    return False #아무것도 겹치지 않으면   False 를 함수에 반환 

#윈도우에 글자 그리기 
def drawText(text,font,surface,x,y):
    textobj = font.render(text,1,TEXTCOLOR) #surface 객체 만들기 
    textrect = textobj.get_rect() #textobj 의 rect값 가져오기 
    textrect.topleft =(x,y) #rect값의 topleft속성에 튜플(x,y)값을 넣어 위치 변경 
    surface.blit(textobj,textrect) #이제 그려 ~ 



#pygame 초기화 하고 윈도우 설정하기 
pygame.init() #게임초기화
mainClock = pygame.time.Clock() #frame 
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) #screen size
pygame.display.set_caption('Chans Dodger') #name 
pygame.mouse.set_visible(False) #마우스 안보이게 해서 플레이어를 안가리게 한다 !

#폰트 설정
font = pygame.font.SysFont(None,48)

# 사운드 설정
gameOverSound = pygame.mixer.Sound("gameover.wav") #소리 = mixer 
pygame.mixer.music.load("background.mid") #배경음악 객체 생성 아님 ! 
#mixer.sound는 새 sound객체를 만들어서 이 객체에 대한 레퍼런스를 변수에 저장 

#이미지 설정
playerImage = pygame.image.load("player.png")
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load("baddie.png")

#시작 화면 보여주기 
windowSurface.fill(BACKGROUNDCOLOR)
drawText("Chans Dodger",font,windowSurface,(WINDOWWIDTH/3),(WINDOWHEIGHT/3))
drawText("Press a key to start.",font,windowSurface,(WINDOWWIDTH/3)-30,(WINDOWHEIGHT/3)+50)
pygame.display.update()
waitForPlayerToPressKey()
#넘겨주는 인자, 1.보여주려고 하는 문자열 2.문자열을 보여줄 때 사용할 폰트, 3.텍스트를 그릴 surface객체, 어디에그릴지 엑스와이 좌표 

#### MAIN ####
topScore = 0 #플레이어가 게임에서 졌을떄 점수 초기화를 위해 시작부터 0으로 초기화한다 
while True :  #플레이어가 매번 새 게임을 시작하도록 하는 와일 문 
    baddies = [] #나쁜이들 리스트는 rect,speed,surface 키를 가진 딕셔너리  
    score = 0 
    playerRect.topleft = (WINDOWWIDTH/2,WINDOWHEIGHT-50) #플레이어의 시작 위치는 화면 가운데, 바닥에서 50 떨어진 곳, (x,y) 튜플이다 !
    moveLeft = moveRight = moveUp = moveDown = False #all False
    reverseCheat = slowCheat = False #치트 False
    baddieAddCounter = 0 #이 값이 증가하면서 ADDNEWBADDIEMRATE 이 값과 일치할때마다 악당 생성 ! 
    pygame.mixer.music.play(-1,0.0) #(먗반,어디서부터?) -1 = 무한실행

    ### GAME LOOP ###
    while True :  #계속 실행 ! 
        score+=1  #그러므로 플레이어가 생존하는 시간이 길수록 점수가 상승하도록 한다 .

        ## EVENT ##
        for event in pygame.event.get(): #pygame 에서 발생하는 모든 이벤트가져왕
            if event.type == QUIT: #event 객체의 type 속성 검사해서 QUIT나오면 실행 
                terminate() # 우리 여기까지만 하자잉 ~ 

            if event.type == KEYDOWN:
                if event.key == ord("z"):
                    reverseCheat = True
                if event.key == ord("x"): #ord를 눌러 아스키 값 -> 파이게임으 키보드 이벤틑는 항상 소문자 아스키값을 사용 
                    slowCheat = True 
                if event.key == K_LEFT or event.key == ord("a"):
                    moveRight = False
                    moveLeft = True 
                if event.key == K_RIGHT or event.key == ord("d"):
                    moveRight = True
                    moveLeft = False 
                if event.key == K_UP or event.key == ord("w"):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord("s"):
                    moveUp = False
                    moveDown = True           
                
            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False 
                    score = 0 #x,z를 누르고 있을때 치트는 되는데 치트 끝날 시  점수 초기화 ㄸ 
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            #마우스 
            if event.type == MOUSEMOTION:
                #마우스를 움직이면 마우스 커서가 있는 곳으로 플레이어를 움직인다. 
                playerRect.move_ip(event.pos[0]-playerRect.centerx, event.pos[1]-playerRect.centery)
                #mouse option pos속성 가진다 move_ip method 렉트 객체를 해당 픽셀 만큼 수직/수평으로 이동 ip = in place 
            
        # 새 악당 추가하기 
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1 # 치트실행중에는 악당생성안함 ㄷㄷ 
        if baddieAddCounter == ADDNEWBADDIEMRATE:
            baddieAddCounter= 0 #0으로 돌리기 
            baddieSize = random.randint(BADDIEMINSIZE,BADDIEMAXSIZE)
            newBaddie = {
                "rect": pygame.Rect(random.randint(0,WINDOWWIDTH - baddieSize),0 - baddieSize, baddieSize, baddieSize), 
                 #x,y,너비 높이 x는 랜덤 y는 화면에 딱맞게 하기위해 악당 크기 빼줌. 
                 "speed":random.randint(BADDIEMINSPEED,BADDIEMAXSPEED),
                 "surface":pygame.transform.scale(baddieImage,(baddieSize,baddieSize)),
    
            }
            baddies.append(newBaddie) #새 악당을 악당리스트에 추가한다. 

        #플레이어 움직이기 
        if moveLeft and playerRect.left > 0 : #플레이어의 왼쪽 모서리 좌표가 0보다 클때 계속 기기 ! 
            playerRect.move_ip(-1*PLAYERMOVERATE,0) # -5는 현재 위치에서 5픽셀 왼쪽 이동
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        
        #플레이어 위치를 맞추기 위해 마우스를 움직인다.
        pygame.nouse.set_pos(playerRect.centerx,playerRect.centery) #마우스 커서를 플레이어의 캐릭터와 같은 위치로 옮긴다.
        #set_pos 는 마우스 커서를 넘겨준 x y 좌표로 옮긴다. -> 점프 방지 

        #악당을 아래로 내린다. 
        for b in baddies : 
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0,b["speed"]) #악당들은 speed키 값에 저장된 속도대로 아래로 이동한다. 
            elif reverseCheat:
                b['rect'].move_ip(0,-5) #위로 가버렷 
            elif slowCheat:
                b['rect'].move_ip(0,1) #천천히 움직여버렷 
        
        #바닥을 지나친 악당 삭제요 ~ 
        for b in baddies[:]: #리스트에 대해 반복중에는 리스트에 아이템 수정 불가 따라서 baddies리스트 복사 해서 반복
            if b['rect'].top>WINDOWHEIGHT:
                baddies.remove(b) #y값이 커질수록 아래로 내려감 이게 트루면 삭제 고고 

        # draw the game world on the window 
        windowSurface.fill(BACKGROUNDCOLOR)
        #이를통해서 이전 게임루프에서 그렸던것을 모두 지워버린당 
        
        #점수와 탑스코어 그리기
        drawText(f'Score :{score}',font,windowSurface,10,0)
        drawText(f"Top Score : {topScore}",font,windowSurface,10,40)

        #플레이어의 캐릭터 그리기 
        windowSurface.blit(playerImage,playerRect) #사진,위치

        #악당을 그린다.
        for b in baddies:
            windowSurface.blit(b['surface'],b['rect']) #baddies list를 하나씩 돌아가며 악당을 그린다
        
        pygame.display.update() #draw game

        #플레이어와 부딪힌 악당이 있는지 검사한다.
        if playerHasHitBaddie(playerRect,baddies): #충돌하면 트루
            if score>topScore:
                topScore = score #topscore초기화 
            break 
            
        mainClock.tick(FPS) #화면속도 늦추기 

    #게임을 멈추고 "GAME OVER"화면을 보여준다.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText("GAME OVER", font, windowSurface,(WINDOWWIDTH/3),(WINDOWHEIGHT/3))
    drawText("Press a key to play again",font,windowSurface,(WINDOWWIDTH/3)-80,(WINDOWHEIGHT/3)+50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()


                

