import random

####### 리스트 정의 시작 ########


# 행맨 그리기/ 리스트 형식 
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
 =========''','''

  +---+
  |   |
  O   |
      |
      |
      |
 =========''','''

  +---+
  |   |
  O   |
  |   |
      |
      |
 =========''','''

  +---+
  |   |
  O   |
 /|   |
      |
      |
 =========''','''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
 =========''','''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 =========''',
 '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 =========''']

# 랜덤단어 
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


####### 함수 정의 시작 ########

#랜덤 단어 하나 추출 
def getRadomWord(wordlist):
    wordIndex = random.randint(0,len(wordlist)-1) #한개의 인덱스 값 선택 (랜딘트의 범위를 words의 길이로 표현했음)
    return wordlist[wordIndex] 

#메인 보드 가져오기 
# miss = 맞추지 못한 문자열, correct = 맞춘 글자의 문자열 ,secret =  맞춰야할 비밀 문자열 
def displayBoard(HANGMANPICS,missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)]) #miss 한 번째의 행맨 사진을 가져온다 
    print()
    
    print("missed Letters:", end=" ")  #단어 놓친 횟수 
    for letter in missedLetters: # 놓친 횟수 포문돌려서 구하기 
        print(letter,end=" ")
    print()

    blanks="_"*len(secretWord) #힌트 
    
    for i in range(len(secretWord)): #맞게 추측한 단어 빈칸을 채우는 과정 / 포문돌리면서 하나씩 비교해가며 단어찾기 
        if secretWord[i] in correctLetters :
            blanks= blanks[:i]+ secretWord[i] + blanks[i+1:] #secretword만 보여주고 나머진 _ 긋기 

    for letter in blanks: #문자와 빈칸으로 비밀 단어 보여주기 
        print(letter, end=' ')
    print() 

def getGuess(alreadyGuessed): #단어 추측하기/ 이미 추측한 단어 제외를 위해 인자를 받아옴. 
    #플레이어가 입력한 글자를 입력한다. 여기에서는 플레이어가 글자 하나를 입력했는지 확인 한다. 
    while True : 
        print("Guess A Letter.")
        guess= input()
        guess= guess.lower() #추측한 단어 소문자 통일 
        if len(guess) != 1: #두스펠링 이상을 입력했을 경우 
            print("Please enter a Single Letter ! ")
        elif guess in alreadyGuessed: #이미 추측했던것 ! 
            print("You have already guessed that letter. Choose Agian")
        elif guess not in "abcdefghijklmnopqrstuvwxyz": #영어가 아닌 경우 ! 
            print("PLEASE Enter A LETTER !!! ")
        else : 
            return guess #추측값 반환 

def playAgain(): #다시할려 ? 
    print("Do you want to play Again ? (Y/N)")
    return input().lower().startswith('y') 

####### 메인 시작 ########
print("H A N G M A N")
missedLetters=" "
correctLetters=" " # 아직 입력안 받았으니 문자열 값 초기화 
secretWord = getRadomWord(words) # 단어 하나 가져와버렷
gameIsDone = False #이것을 기준으로 다시 시작할지 안할지 끝에 물어봄 

while True : 
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)

    #플레이어 문자입력 
    guess = getGuess(missedLetters + correctLetters) # 틀리고 맞았던 스펠링들 

    if guess in secretWord:
        correctLetters = correctLetters + guess 

        #플레이어가 이김? 
        foundAllLetters = True 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False 
                break
        if foundAllLetters:
            print(f"yes secretWord is {secretWord} You have won")
            gameIsDone = True 
    else :
        missedLetters = missedLetters + guess 
        if len(missedLetters) == len(HANGMANPICS)-1 :
                displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
                print(f"You lost, the word is {secretWord}")
                gameIsDone = True
        
    if gameIsDone: #gmaeIsDone 이 트루이다 ! 
        if playAgain():
                missedLetters=" "
                correctLetters=" "
                gameIsDone = False
                secretWord = getRadomWord(words)
        else : 
            break 

# 키보드 겁나 편해요 사기 잘했어요 이제 맥북 키보드는 안써도 되는건가요 ?이게 맥북은 두고 키보드를 연결해서 쓰는 맛이군요... 아마 곧 스크린도 사게 될까 ??
###use dictionary 를 활용하여 사용자에게 장르 선택 권한을 준다. 그리고 그 장르 key 안의 값들에서 선택할 수 있게 한다 ! <<< 추가 기능들 . 