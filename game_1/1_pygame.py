import random

guessesTaken = 0

print("Hello What is your name?")
myName = input()

number = random.randint(1,20)
print(f"Well, {myName}, I am thinking of a number between 1 and 20.")

while guessesTaken<6:
    print(f"Take a guess u left {6-guessesTaken} times")
    guess= input()
    guess = int(guess)

    guessesTaken += 1
    if guess< number:
        print("You Low")
    elif guess>number:
        print("You high")
    else:
        break
if(guess==number):
    guessesTaken=str(guessesTaken)
    print(f"good u have {guessesTaken} times ")

if guess != number :
    number=str(number) 
    print(f"noob i think {number}")   