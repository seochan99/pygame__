import random 

#베이글 게임 ### 숫자 3개 0~9를 중 다른거 세개를 추출 해야한다.
def getSecreNum(numDigits): #파라미터값 만큼 비밀번호를 만든다 
    # numDigits 길이만큼의 문자열을 반환한다. 이 문자열은 임의의 숫자로 이루어져 있으며 모두 다르다. 
    numbers = list(range(10)) #list 10개 -> range()함수는 리스트를 반환하지 않고 iterator객체를 반환하기 땨문이다./ 
    #for문에서는 써도 되지만 변수에 정수의 리스트를 저장하려면 range()반환값을 list()함수를 통해 리스트로 바꿔  (0~9)숫자    
    random.shuffle(numbers) #number의 순서를 무작위로 바꾼다 -> list자체를 변경한다 
    secretNum = " " #비밀번호는 숫자에서 3개를봅아서 만든다. 
    for i in range(numDigits): # numDigits만큼 iqksqhr 
        secretNum += str(numbers[i]) #SecretNum에 Numbers를 붙여나간다 !!! 넘디짓만큼이니깐 3개의 숫자 ! 
    return secretNum #비밀번호 반환 ! 

def getClues(guess,secretNum):
    #pico, fermi, bagels 문자열로 된 힌트를 반환한다. 
    if guess == secretNum : 
        return "You Got It !!!"
    clue = []

    for i in range(len(guess)): #추측한 길이만큼 ! = 넘디짓 길이지 !
        if guess[i] == secretNum[i]:
            clue.append("Fermi") #위치 숫자 모두 일치  각자리위치! 
        elif guess[i] in secretNum: # 게스 [i]와 비밀번호 3자리 모두 비교 ! 
            clue.append("Pico") #숫자만 일치 위치 X 
    if len(clue)==0:
        return "Bagels" # clue길이가 0일때 즉, 아무것도 맞추지 못했을때 !

    clue.sort() #리스트를 알파벳과 숫자 순서로 정렬해 준다. 리스트 자체를 정렬. sort자체는 None을 반환한다. 이를 통해 순서대로 단서를 주는것이 아니라 알파벳순으로 줘서 게임을 더 어렵게 만든다. 
    return " ".join(clue) #clue리스트 사이에 빈칸을 넣는다 ! => 조금더 이쁘게 출력한다.  
def isOnlyDigits(num):
    #num이 숫자로 이루어진 문자열이면 True를 반환한다. 그렇지 않으면 False를 반환한다.
    if num == " ":
        return False 
    for i in num:
        if i not in "0 1 2 3 4 5 6 7 8 9".split(): 
            return False 

    return True

def playAgain():
    #플레이어가 또 게임을 하고자 하면 True 를 반환하고, 아니면 False 를 반환한다. 
    print("Do you want to play Again? (Y/N)")
    return input().lower().startswith("y") # y로 시작하는게오면 트루를 반환한다 ! 


##########  Main ##########
NUMDIGITS = 3
MAXGUESS = 10 #이를 통해서 언제든지 쉽게 문자열의 길이나 기회를 수정할 수 있다. 

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while True:
    secretNum = getSecreNum(NUMDIGITS) #비밀번호 생성 
    print("I have Thought up a number. You have %s guesses to get it." %(MAXGUESS)) #너는 이만큼 기회 있음 

    numGuesses = 1
    while numGuesses <= MAXGUESS :#추측한 횟수가 최대 기회보다 낮을때 !
        guess = " " #guess 초기화 
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess): #guess의 길이가 NUMDIGITS보다 짧거나! isonly함수에 의해서 숫자가 아닌 값이 입력되었을때 False 를 반환한다 ! 
            print("Guess #%s: " %(numGuesses))
            guess = input()


        clue = getClues(guess,secretNum) #힌트주기 
        print(clue) # give clue ! 
        numGuesses += 1 #밎춘횟수 1개 늘리기 

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print("You ran out of guesses. The answer was %s" %(secretNum))

    if not playAgain(): #트루를 반환한다 ! 그러면 if ture -> False back.  
        break 