#Hangman game
#Designed by AnirudhCB @AllTheGoodNamesAreGone and AriaVikram @Caffetaria
#Credit for the hangman image goes to https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman

import random
import time
diag = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",

"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",

"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

#print (word)

nameusr = raw_input("Enter your name, brave contestant: ")
print("Welcome, {}, to HANGMAN. Be wary. \nKeep your wits about you, for this is no simple feat. \n".format(nameusr))
time.sleep(2)
print("Eight Chances...Eight is all you've got to guess the word.\nEverything depends on this.")
time.sleep(2)
print("This is it. No turning back. LET THE GAME BEGIN...")

guess = None
allguesses = []
joinedword = None
wordguessed = []


 
def rulecheck():
    rule = raw_input("If you are aware of the rules, press 2. If not, press 1: ")
    if rule =="1" :
        print("Very well. Here are the rules for this game of wits\n")
        time.sleep(1)
        print("A word will be generated by the computer. \nYour job is to guess letters of that word, one by one, until you figure the word out.")
        time.sleep(1)
        print("\nFor every wrong guess, you come one step closer to losing. Good luck.")
        #mainlog(word)    
    elif rule=="2":
        print "Good. Lets go."    
    else :
        print("Sorry, I have no clue what you mean. Care to repeat?") 
        rulecheck()
       # mainlog(word)  


def mainlog():
    x = ["Apples", "Bananas", "Oranges", "Football", "Batman", "Manchester", "Martian", "Fortran"]
    list1 = x

    rnum = random.randint(0,len(list1) -1)
    word = x[rnum].lower()
    for x in word:
        wordguessed.append('-')
    attempts = 0
    print("Hold on please. Generating random words...")
    time.sleep(2)
    print ("Calculating probabilities...")
    time.sleep(2)
    print("All right! We are good to go.")
    
    print (diag[0])
    attempts = len(diag) -1
    
    while attempts !=0: 
        joinedword = "".join(wordguessed)
        print(("You have {} attempts remaining. ").format(attempts))
        print(joinedword)
        
        try:
            guess = str(raw_input("Enter your guess. Any letter in the alphabet: \n")).lower()
        except: 
            print("\nWait a minute...Invalid input!. Try again.")
            continue
        else:
            if len(guess)>1:
                print("\nOnly one letter at a time. Try again.")
                continue
            elif not guess.isalpha():
                print("Sorry, non-alphabet inputs are not welcomed here. Try again.")
                continue
            elif guess in allguesses:
                print("Word already guessed. Please try again.")
                continue
            else:
                pass
            
        allguesses.append(guess)
        for count in range (len(word)):
            if guess ==word[count]:
                wordguessed[count] = guess
                print("On the spot! Good guess")
        if guess not in word:
                attempts-=1
                print("OOOH! That was a close one, but your guess was wrong!")
                print(diag[(len(diag)-1)-attempts])
                
        if "-" not in wordguessed:
           
                print("Well, well, well... Nice game, {}. You have conquered the mighty hangman!/nKudos to you. ".format(nameusr))
                time.sleep(1)
                print("The word was indeed {}!".format(word))
                break
    if attempts == 0:
            print("GAME OVER!!! YET another falls to the unconquerable HANGMAN. \n Fear not, for you are not the first to face this predicament.")
            print("The word that you failed to guess was: {}".format(word))
    #fin= raw_input("Would you like to test your skills once again, {}? Type in yes/no:".format(nameusr)).lower()
    #if fin =="yes":
     #   mainlog()
    #elif fin =="no":
    time.sleep(2)
    print("Good day to you, {}. Farewell on your further conquests. ".format(nameusr))
    quit      
                
    
rulecheck()
mainlog()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        



