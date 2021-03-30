##input을 쓰지않는다 -> 더 이상 텍스트로 입력과 출력을 하지않는다. 대신 윈도우에 그래픽이나 텍스트를 그려서 결과를 보여준다,.
#마우스나 키보드 이용 -> 이벤틑 
import pygame, sys
from pygame.locals import * #local모듈은 파이겜에서 사용하는 많은 상수 변수를 가지고 있다. 

#pygame 설정
pygame.init() #pygame함수들은 호출 하기전에 pygame.init()을 수행해야한다. 

# 윈도우 설정 
windowSurface = pygame.display.set_mode((500,400),0,32) #((가로,세로),0,컬러 깊이)
pygame.display.set_caption("Hello World!!") 

# 색깔 설정
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#폰트 설정 
basicFont = pygame.font.SysFont(None,48)# (폰트이름,폰트크기)

#setting text
text = basicFont.render("Hello World!",True,WHITE,BLUE) #(그릴문자열, 안티 엘리어싱 사용?,)
textRect = text.get_rect()  #pygame.Rect(left,top,width,height)
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#surfacce background white 
windowSurface.fill(WHITE)

#surface에 초록색 다각형 그리기
pygame.draw.polygon(windowSurface,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))

#surface에 파란색 원 그리기
pygame.draw.circle(windowSurface,BLUE,(300,50),20,0)

#surface에 빨간색 타원 그리기
pygame.draw.ellipse(windowSurface,RED,(300,250,40,80),1)

#surface 에 텍스트의 배경 사각형 그리기
pygame.draw.rect(windowSurface,RED,(textRect.left - 20, textRect.top-20, textRect.width+40,textRect.height+40))

#surface의 픽셀 배열 얻어 오기
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# surface에 텍스트 그리기 
windowSurface.blit(text,textRect)

#draw window in screen
pygame.display.update()

#play game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()

