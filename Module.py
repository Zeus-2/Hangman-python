# - - - Repos - - -
#Used to randomly selected a word
import random
#Reads and writes CSV file
import csv
#Used to sort list
from operator import itemgetter


#Fetches a random word from Words.CSV
def fetchWord():
  #Opens and closes Words.csv
  with open('Words.csv') as Raw:
    #sets the raw data as "Data"
    Data = csv.reader(Raw, delimiter=',')
    #Converts the Raw data to a list
    Data = list(Data)

  #Picks a rando row from Words.csv.
  #Column 0 = Word
  #column 1 = Hint
  Row = (random.choice(Data))

  #Returns Word and Hint
  return Row[0],Row[1]


#Orbfuscates the word by replacing each letter with "-"
def obfuscate(Word):
  return ("-" * len(Word))


#Checks if guessed word = to word
def guessWholeWord(Guess, Word):
  #Compares Guess and Word in lowercase
  if str(Guess).lower() == Word.lower():
    return True
  else:
    return False


#replaces "-" with guessed letters
def CheckWord(Word, WordGuessed, OrbfuscatedWord):
  #Makes sure the word that being compared is lowercase
  Word = Word.lower()
  WordGuessed = str(WordGuessed).lower()

  #If the
  if WordGuessed in Word:
    #Splits the string into a list
    OrbfuscatedWord.split()
    #Iterates through Word
    for Counter in range(0, len(Word)):
      if Word[Counter] == WordGuessed:
        # Splits the string into a list
        Word.split()
        OrbfuscatedWord = [*OrbfuscatedWord]
        OrbfuscatedWord[Counter] = Word[Counter]
    return "".join(OrbfuscatedWord)
  else:
    return OrbfuscatedWord


#Input validation
def InputValidation():
  #Loops until a valid input is entered
  while True:
    Word = input("Guess one letter: ")
    #Checks if the word is alphanumeric
    if Word.isalpha() == True:
      return Word
    #If the input isnt alphanumeric
    else:
      print("Please only enter letters.")

  while Word.isalpha == False:
    Word = input("Guess a letter: ")


#Writes a new line to scoreboard.csv
def WriteScoreboard(Username, Tries):
  #Opens and closes ScoreBoard.csv
  with open('ScoreBoard.csv', 'a') as Raw:
    #Reads the CSV file and stores it as writer
    writer = csv.writer(Raw)
    #Append a row with username and score
    writer.writerow([Username, Tries])

#Writes
def DisplayScoreboard():
  Counter = 0
  #Opens and closes ScordBoard.csv
  with open('ScoreBoard.csv') as Raw:
    #Reads Scorebaord.csv and stores as Data
    Data = csv.reader(Raw, delimiter=',')
    #Converts Raw data and formats into a list
    Data = list(Data)

  #Sorts the list by score
  Data = sorted(Data, key=itemgetter(1), reverse=False)
  print("\n-=-=-=- Scoreboard -=-=-")
  print("    Username - Tries")

  #Iterates through the list
  for Row in Data:
    Counter = Counter + 1
    #Outputs sorted list per row in nice clean format
    print(str(Counter) + ".)", Row[0], "-", Row[1])
    #Checks if its iterated 5 times
    if Counter == 5:
      print("-=-=-\n")
      #Breaks out of the code
      return
  print("-=-=-\n")