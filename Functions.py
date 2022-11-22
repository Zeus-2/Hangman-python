#Repos
import random

#Matthew Lacey
def FetchWord():
    f = open("Words.txt","r")
    words = f.readlines()
    f.close()

    return (random.choice(words)).rstrip("\n")
