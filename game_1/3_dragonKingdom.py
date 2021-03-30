# 1. 함수
# 2. 수 만드는 법, 함수 호출
# 3. 반환값, 변수영역(지역/전역)
import random
import time

def display():
    print("you choose cave 1 or 2")
    print("one is angel, other is evil")

def chooseCave():
    cave = " "
    while cave != "1" and cave != "2":
        print("1 or 2")
        cave =input()
    return cave
1
def cehckCave(chosenCave):
    print("You ... approach")
    time.sleep(2)
    print("hmmm..")
    time.sleep(2)
    print("who come here!!")
    print()
    time.sleep(2)

    angle = random.randint(1,2)
    if chosenCave == str(angle):
        print(" hi angle")
    else:
        print(" You Die IM Evil!!!")
    print()


playAgain = "yes"
while playAgain == "yes" or playAgain =="y":
    display()
    caveNumber = chooseCave() #return 값을 caveNjumber 에 넣는다.
    cehckCave(caveNumber)
    print("replay? Y/N")
    playAgain=input().lower()

