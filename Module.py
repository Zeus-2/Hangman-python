#Repos
import random
import csv


#Matthew Lacey
def fetchWord():
  with open('Words.csv') as Raw:
    Data = csv.reader(Raw, delimiter=',')
    Data = list(Data)
  Row = (random.choice(Data))

  return Row[0],Row[1]


#Matthew Lacey
def obfuscate(Word):
  return ("-" * len(Word))


#Matthew Thomas
def guessWholeWord(Guess, Word):
  if str(Guess).lower() == Word.lower():
    return True
  else:
    return False


#Matthew Lacey
def CheckWord(Word, WordGuessed, OrbfuscatedWord):
  Word = Word.lower()
  WordGuessed = str(WordGuessed).lower()
  if WordGuessed in Word:
    OrbfuscatedWord.split()
    for Counter in range(0, len(Word)):
      if Word[Counter] == WordGuessed:
        Word.split()
        OrbfuscatedWord = [*OrbfuscatedWord]
        OrbfuscatedWord[Counter] = Word[Counter]
    return "".join(OrbfuscatedWord)
  else:
    return OrbfuscatedWord


# Matthew Thomas
def InputValidation():
  while True:
    Word = input("Guess one letter: ")
    if Word.isalpha() == True:
      return Word
    else:
      print("Please only enter letters.")

  while Word.isalpha == False:
    Word = input("Guess a letter: ")


#Matthew Lacey
def WriteScoreboard(Username, Tries):
  with open('ScoreBoard.csv', 'a') as Raw:
    writer = csv.writer(Raw)
    writer.writerow([Username, Tries])


#Matthew Lacey
def DisplayScoreboard():
  Counter = 0
  with open('ScoreBoard.csv') as Raw:
    Data = csv.reader(Raw, delimiter=',')
    Data = list(Data)

  print("\n-=-=-=- Scoreboard -=-=-")
  print("    Username - Tries")
  for Row in Data:
    Counter = Counter + 1
    print(str(Counter) + ".)", Row[0], "-", Row[1])
  print("-=-=-\n")