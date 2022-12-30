#Exstenal Module which has the following sub functions
#FetchWord - Gets a random word from Words.csv
#guessWholeWord - Validation check to see if the whole word is guessed
#CheckWord - Compares word against orbfuscated word
#InputValidation - Input validation when guessing the letters
#WriteScoreboard - Write username and attempts to ScoreBoard.csv
#DisplayScoreboard - Scoreboard reads, sorts and, displays the scoreboard
import Module


def main():
    #Variable is used to iritate through the main game loop
    play = True
    #Module FetchWord gets a random word and hint from Words.csv and stores it as word variable
    word = Module.fetchWord()
    #The following two variables split the variable word
    hint = word[1]
    word = word[0]

    #Simple string to store the users username
    username = input("Username:")
    #Function orbfuscate replaces every charater in the string with "-"
    obfuscateWord = Module.obfuscate(word)
    #Simple counter to record the ammount of rounds
    tryCounter = 0

    while play:
        #Iterate counter to record rounds
        tryCounter += 1
        print("\n-=-=- Try", tryCounter, "-=-=-")
        print("CHEATER!", word)
        print("Word:", obfuscateWord)
        #Module InputValidation gets a input from the user and validates it, once validated its stored as the string "guess"
        guess = Module.InputValidation()
        #Replaces "-" with a letter. so the user can knows what they have guessed.
        obfuscateWord = (Module.CheckWord(word, guess, obfuscateWord))

        #Checks if you have guessed all the letters
        if Module.guessWholeWord(str(obfuscateWord), word) is True or Module.guessWholeWord(guess,word) is True or Module.guessWholeWord(str(obfuscateWord), word) is True:
            print("You have guessed all the letters")
            #Writes the score to the exsternal ScoreBoard.csv file
            Module.WriteScoreboard(username, tryCounter)
            #End the loop of the game
            play = False
        else:
            #Records user input
            userInput = input("Would you like a hint? Input:")
            #Variable for the next loop
            loop = True
            while loop:
                #Checks if the user wants a hint
                #If they want a hint following code will run
                if userInput.lower() == "yes" or userInput.lower() == "y":
                    print("Hint:", hint)
                    #Breaks out of the loop
                    loop = False
                #If the user doesnt want a hint the following code will run
                elif userInput.lower() == "no" or userInput.lower() == "n":
                    #Breaks out of the loop
                    loop = False
                #Invalid answer
                #Lets the user know the guess is invalid and they should guess again.
                else:
                    print("Invalid input, please enter only Yes or No")
                    break


def menu():
    #Simple menu system
    #Each number corrisponds to feature of the game
    print("-=-=- Main menu -=-=-")
    print("Please pick one of the following numbers")
    print("1.) Play")
    print("2.) Scoreboard")
    print("3.) How to Play")

    #Checks users response
    while True:
        choice = input("Number: ")
        #If the response is valid
        if choice in ["1", "2", "3"]:
            return choice
        #If the response is invalalid it will let the user know and ask for another response
        else:
            print("Invalid response, you need to pick a the number that relates to a option. Please try again")


if __name__ == '__main__':
    #Variable for the loop
    play = True
    while play:
        #Runs the menu and gets a response for the feature of the game to be run
        choice = menu()

        #Checks which section of the code should be used
        if choice == "1":
            main()
            #Loop the variable
            Valid = False
            while Valid:
                print("-=-=-")
                print("Would you like to play again?")
                print("Type Y for Yes or N for No")
                #Records player input
                PlayChoice = input("Choice: ")

                #Check if the user said yes
                if PlayChoice.upper() == "Y" or PlayChoice.upper() == "YES":
                    print("-=-=- New Game -=-=-")
                    #Breaks out of the loop
                    Valid = True

                #Checks of the user said no
                elif PlayChoice.upper() == "N" or PlayChoice.upper() == "NO":
                    #Breaks out of the loop
                    Valid = True
                    play = False

                #If the response is invalid
                else:
                    print(
                        "Invalid response, you need to pick either 'Y' for Yes or 'N' for No"
                    )
        #If the user picked 2nd option
        elif choice == "2":
            #Displays scoreboard
            Module.DisplayScoreboard()

        #if the user picked 3rd option
        elif choice == "3":
            #outputs help commandi
            print("\n-=-=- How to play! -=-=-\nA word will be randomly generated then you will have to guess each letter until you can guess the full word.\ngoodluck!\n-=-=-=-\n")
