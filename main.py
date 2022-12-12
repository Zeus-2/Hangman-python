#Dependancies
import Module


def main():
    play = True
    word = Module.fetchWord()
    hint = word[1]
    word = word[0]

    username = input("Username:")
    obfuscateWord = Module.obfuscate(word)
    tryCounter = 0
    while play:
        tryCounter += 1
        print("\n-=-=- Try", tryCounter, "-=-=-")
        print("CHEATER!", word)
        print("Word:", obfuscateWord)
        guess = Module.InputValidation()
        obfuscateWord = (Module.CheckWord(word, guess, obfuscateWord))
        if Module.guessWholeWord(str(obfuscateWord), word) is True or Module.guessWholeWord(guess,word) is True or Module.guessWholeWord(str(obfuscateWord), word) is True:
            print("You have guessed all the letters")
            Module.WriteScoreboard(username, tryCounter)
            play = False
        else:
            userInput = input("Would you like a hint? Input:")
            loop = True
            while loop:
                if userInput.lower() == "yes" or userInput.lower() == "y":
                    print("Hint:", hint)
                    loop = False
                elif userInput.lower() == "no" or userInput.lower() == "n":
                    loop = False
                else:
                    print("Invalid input, please enter only Yes or No")
                    break


def menu():
    print("-=-=- Main menu -=-=-")
    print("Please pick one of the following numbers")
    print("1.) Play")
    print("2.) Scoreboard")
    print("3.) How to Play")
    while True:
        choice = input("Number: ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid response, you need to pick a the number that relates to a option. Please try again")


if __name__ == '__main__':
    play = True
    while play:
        choice = menu()

        if choice == "1":
            main()
            Valid = False
            while Valid:
                print("-=-=-")
                print("Would you like to play again?")
                print("Would you like to play again?")
                print("Type Y for Yes or N for No")
                PlayChoice = input("Choice: ")
                if PlayChoice.upper() == "Y" or PlayChoice.upper() == "YES":
                    print("-=-=- New Game -=-=-")
                    Valid = True
                elif PlayChoice.upper() == "N" or PlayChoice.upper() == "NO":
                    Valid = True
                    play = False
                else:
                    print(
                        "Invalid response, you need to pick either 'Y' for Yes or 'N' for No"
                    )

        elif choice == "2":
            Module.DisplayScoreboard()
        elif choice == "3":
            print("\n-=-=- How to play! -=-=-\nA word will be randomly generated then you will have to guess each letter until you can guess the full word.\ngoodluck!\n-=-=-=-\n")
