import Module

def Main():
  Play = True
  Word = Module.FetchWord()
  Username = input("Username:")
  OrbfuscatedWord = Module.Orbfuscate(Word)
  TryCounter = 0
  while Play == True:
    TryCounter += 1
    print("\n-=-=- Try", TryCounter, "-=-=-")
    print("CHEATER!", Word)
    print("Word:", OrbfuscatedWord)
    Guess = Module.InputValidation()
    OrbfuscatedWord = (Module.CheckWord(Word, Guess, OrbfuscatedWord))
    if Module.guessWholeWord(str(OrbfuscatedWord), Word) == True or Module.guessWholeWord(
        Guess, Word) == True or Module.guessWholeWord(str(OrbfuscatedWord),
                                               Word) == True:
      print("You have guessed all the letters")
      Module.WriteScoreboard(Username, TryCounter)
      Play = False
    #Guess = InputValidation()

    #print(OrbfuscatedWord)
    #print(Word)


def Menu():
  print("-=-=- Main menu -=-=-")
  print("Please pick one of the following numbers")
  print("1.) Play")
  print("2.) Scoreboard")
  print("3.) How to Play")
  while True:
    Choice = input("Number: ")
    if Choice in ["1", "2", "3"]:
      return Choice
    else:
      print(
        "Invalid response, you need to pick a the number that relates to a option. Please try again"
      )


if __name__ == '__main__':
  Play = True
  while Play == True:
    Choice = Menu()

    if Choice == "1":
      Main()
      Valid = False
      while Valid == False:
        print("-=-=-")
        print("Would you like to play again?")
        print("Type Y for Yes or N for No")
        PlayChoice = input("Choice: ")
        if PlayChoice.upper() == "Y" or PlayChoice.upper() == "YES":
          print("-=-=- New Game -=-=-")
          Valid = True
        elif PlayChoice.upper() == "N" or PlayChoice.upper() == "NO":
          Valid = True
          Play = False
        else:
          print(
            "Invalid response, you need to pick either 'Y' for Yes or 'N' for No"
          )

    elif Choice == "2":
      Module.DisplayScoreboard()
    elif Choice == "3":
      print(
        "\n-=-=- How to play! -=-=-\nA word will be randomly generated then you will have to guess each letter until you can guess the full word.\nGoodluck!\n-=-=-=-\n"
      )