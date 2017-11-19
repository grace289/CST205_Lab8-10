  #!/usr/bin/python
MAX_ALLOWED_ATTEMPTS = 6
PUZZLE_WORD_LIST = [ "parrot", "spam", "nudge", "silly", "cheese", "lumberjack", "argument"]
MSG_USED_GUESSES = "You have used %i of six guesses"
MSG_ALPHA_CHARS_ONLY = "Letters only please!"
MSG_DUPLICATE_CHAR_GUESSED = "You have already guesses %s, please try a different letter."
MSG_GAME_OVER_PLAYER_LOOSES = "Sorry, you lose.  Better luck next time!"
MSG_USER_INPUT_NEEDED = "Enter a guess: "
MSG_ASK_IF_PLAY_AGAIN = "Would you like to play again, enter Y for Yes or N for No: "
MSG_USER_LOST = "Sorry, you lost the word was %s"
MSG_USER_WON = "You guessed correctly!"
MSG_WELCOME = '''
CST205 Lab 10
Pair Programming exercise by:
\tGrace Alvarez
\tGabriel Loring\n
Members of Team 5, Hopper
\tJose Garcia Ledesma
\tGrace Alvarez
\tChristian Guerrero
\tGabriel Loring

Hangman game\n
Try to guess the Montey Python Sketch \nrelated word in %i or fewer tries
\nRules:
\t1.\tOnly Alpha chachters are allowed
\t2.\tRepated charachters are not counted against the player
\t3.\tHave fun
'''

def cleanInput(dirtyString=""):
    '''
    The user input needs to be a A-Za-z
    alpha charachter.  Since we may have 
    spaces and other non alphas, we walk
    through the input string until we find 
    our first alph and return it, if no
    alpha is found return a empty string
    '''
    cleanChar = ""
    for char in dirtyString:
        if char.isalpha():
            cleanChar = char
            break

    return cleanChar

def testLetter(puzzelWord="", userGuess=""):
    '''
    This function tests to see if the guess
    letter is in the puzzle word independent
    of charachter case
    '''
    if userGuess.lower() in puzzelWord.lower():
        return True
    return False

def drawGameScreen(hangmanState=0,puzzelMessage="",statusMsg=""):
    print(MSG_USED_GUESSES%hangmanState)
    print(puzzelMessage)
    print(statusMsg)
    print("\n")
    return

def getUserInput(message="Please enter a letter to test"):
    userString = requestString(message)
    return userString 

def welcomeMessage():
    print(MSG_WELCOME%MAX_ALLOWED_ATTEMPTS)
    

def gameLoop(wordIndex):
    gameWon = False
    gameLost = False
    guessedLetters = []
    gameOver = False
    statusMsg = "_ "*len(PUZZLE_WORD_LIST[wordIndex])
    puzzelWord = PUZZLE_WORD_LIST[wordIndex]
    inccorectGuessCount = 0
    puzzelMessage = "Begin Game"
    while gameWon == False and gameLost == False:
        drawGameScreen(hangmanState=inccorectGuessCount,puzzelMessage=puzzelMessage,statusMsg=statusMsg)

        #Prompt user for input
        dirtyString = getUserInput(MSG_USER_INPUT_NEEDED)
        userGuess = cleanInput(dirtyString)
        if userGuess in guessedLetters:
            puzzelMessage = (MSG_DUPLICATE_CHAR_GUESSED % userGuess) #promt that already guessed
            continue
        elif userGuess in statusMsg:
            puzzelMessage = MSG_ALPHA_CHARS_ONLY  #prompt already found
            continue
        elif userGuess == "":
            puzzelMessage = MSG_ALPHA_CHARS_ONLY
            continue
        else:
            guessedLetters.append(userGuess)

        result = testLetter(puzzelWord=puzzelWord,userGuess=userGuess)
        if result == False:
            inccorectGuessCount = inccorectGuessCount + 1
            puzzelMessage = (MSG_DUPLICATE_CHAR_GUESSED%guessedLetters)
        else:
            puzzelMessage = MSG_USER_WON
            posCount = 0
            s = list(statusMsg)
            for x in puzzelWord:
                if x == userGuess:
                    s[posCount*2] = userGuess
                posCount = posCount + 1
            statusMsg = "".join(s)

        if '_' not in statusMsg:
            gameWon = True
            drawGameScreen(hangmanState=inccorectGuessCount,puzzelMessage=puzzelMessage,statusMsg=statusMsg)

        if inccorectGuessCount == MAX_ALLOWED_ATTEMPTS:
            gameLost = True
            drawGameScreen(hangmanState=inccorectGuessCount,puzzelMessage=puzzelMessage,statusMsg=statusMsg)

    return gameWon

def hangman(): 
    welcomeMessage()
    wordCount = 0
    continueGame = True
    while continueGame == True:
        if gameLoop(wordCount):
            print(MSG_USER_WON)
        else:
            print(MSG_USER_LOST%PUZZLE_WORD_LIST[wordIndex])
        if wordCount < len(PUZZLE_WORD_LIST):
            wordCount = wordCount + 1
        else:
           wordCount = 0
        play_again = cleanInput(getUserInput(MSG_ASK_IF_PLAY_AGAIN))
        print(play_again)
        if play_again.upper()  != 'Y':
            continueGame = False

hangman()