##########
#
#  Submission 2
#  Matthew Eng
#  Dec. 5, 2022
#  Objective: Complete the code for Main.py to establish the game

import pygame
import draw
import cmpt120image
import random

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

### Functions ###
def checkInt(value):
    while not value.isdigit():
        value = input("Please input a valid integer: ")
    return int(value)

def initWordList(numWords,file):
    wordList = []
    file.seek(0)

    for _ in range(numWords):
        word = file.readline()
        wordList.append(word.replace("\n",""))
    
    return wordList

def getRandomModification(img):
    color = [random.randint(0,200),random.randint(0,255),random.randint(0,255)]
    result = draw.recolorImage(img,color)
    if random.choice([True,False]):
      result = draw.minify(result)
    if random.choice([True,False]):
      result = draw.mirror(result)
      
    return result       

def showWords(wordList,w,h):
    cnvs = cmpt120image.getWhiteImage(w,h)
    numSelectedWord = 0
    for i in range(len(wordList)):
        img = cmpt120image.getImage(f"images/{wordList[i]}.png")
        item = getRandomModification(img)
        n = random.randint(1,4)
        draw.distributeItems(cnvs,item,n)

        if i == len(wordList) - 1:
            numSelectedWord = n
            cmpt120image.showImage(cnvs)
            playSound(wordList[i],ENV)

    return numSelectedWord

### End of Functions ###

### Game Settings ###
numWords = 3
inGame = True
menuList = ["Learn - Word Flashcards",
            "Play - Seek and Find Game",
            "Settings - Change Difficulty",
            "Exit"]
wordFile = "blackfoot.csv"
wordList = []
file = open(wordFile)
w=500
h=500
### End of Game Settings ###

### Main ###
while inGame:
    print("\nMAIN MENU")
    for i in range(len(menuList)):
        print(f"{i+1}. {menuList[i]}")
    wordList = initWordList(numWords,file)
    uOption = checkInt(input("\nChoose an option: "))

    if uOption == 1:
        # Learn Section
        for i in range(len(wordList)):
            fileName = wordList[i]
            img = cmpt120image.getImage(f"images/{fileName}.png")
            cnvs = cmpt120image.getWhiteImage(w,h)
            draw.distributeItems(canvas=cnvs,item=img,n=1)
            cmpt120image.showImage(cnvs)
            playSound(fileName,ENV)
            input(f"{i+1}. Presss Enter to continue... ")
    
    elif uOption == 2:
        # Play Section
        print("\nPLAY\nThis is a seek and find game. You will hear a word.")
        print("Count how many of that item you find!\n")
        uRound = checkInt(input("How many rounds would you like to play? "))

        for _ in range(uRound):
            selectedWords = random.sample(wordList,3)
            ans = showWords(selectedWords,w,h)
            uAns = checkInt(input("Listen to the word. How many of them can you find? "))
            if uAns == ans:
                input("Right! Press Enter to continue.\n")
            else:
                input(f"Sorry there were {ans} Please press Enter to continue...\n")

    elif uOption == 3:
        # Settings
        print(f"You are currently learning {numWords} words!")
        
        numWords = checkInt(input("How many would you like to learn (3-12)? "))
        if numWords > 12 or numWords < 3:
            print("Sorry, that's not a valid number. Resetting to 3 words.")
            numWords = 3

    elif uOption == 4:
        # Exit
        inGame = False
        print("Goodbye!")

    else:
        print("\nYour response is not recognized. \nHere is the list of valid responses:")

### End of Main ###
