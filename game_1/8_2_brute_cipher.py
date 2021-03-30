# Caesar Cipher 


### constant ###
MAX_KEY_SIZE = 26

### function ###
def getMode():
    while True:
        print("Do you wish to encrypt or decrypt a meesage?")
        mode = input().lower()
        if mode in "encrypt e decrypt d brute b".split(): #ths = ["encrypt","e" ...  ] list ! 
            return mode
        else : 
            print("Enter either encrypt or e or decrypt or d or brute or b!!!")

def getMessage():
    print("Enter your Message : ")
    return input()

def getKey():
    key = 0
    while True:
        print("Enter the key number (1-%s)" %(MAX_KEY_SIZE))
        key = int(input()) # input으로 받는 값은 문자열 이기에 숫자로 전환을 해줘야지 키값이 정수가 된다 .
        if (key>=1 and key<= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd': # 해독 ㄱㄱ 
        key = -key # 해독에서는 키 값을 음수로 ! 
    translated = '' #이 변수에 문자열을 붙여 나간다

    for symbol in message: #문자열 하나하나 바꾸기 
        if symbol.isalpha(): #문자열이 대소문자 알파벳이면 트루 반환 아니면 폴스 
            num = ord(symbol) #문자열의 아스키값을 받는다. 
            num += key #받아서 키 값만큼 올린다 

            if symbol.isupper(): #대문자있으면 트루 
                if num > ord('Z'): 
                    num -= 26 #Z보다 커지면 문자가아닌 것이 출력되기때문에, 알파벳은 26개 있으므로 26만큼 빼준다. 
                elif num < ord('A'): 
                    num += 26
            elif symbol.islower(): #소문자 있으면 트루 
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'): #a보다 작아지면 안되니깐 플러스 시킨당 ~ 
                    num += 26

            translated += chr(num)
        else:
            translated += symbol #글자가 아닌 심볼은 그냥 붙인다 ! 
    return translated    

### Main ###

mode = getMode()
message = getMessage()
if mode[0] != "b":
    key = getKey()
print("Your Translated text is :")

if mode[0] != "b":
    print(getTranslatedMessage(mode,message,key))
else: 
    for key in range(1,MAX_KEY_SIZE+1):
        print(key, getTranslatedMessage('decrypt',message,key)) #해독한다 그런데! 키를 1-26까지 돌린다 ! 