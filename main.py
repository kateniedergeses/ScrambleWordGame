# Word Scramble
# Kate Niedergeses
# September 10, 2021 start time noon
# End time: 12:32

from random import shuffle
import random
from datetime import date


def scramble(word):
    word = word.strip()
    l = list(word)
    shuffle(l)
    word = ''.join(l)
    return str(word)


def main():
    # read in from file
    fileName = "words"
    # save as variable
    textFile = open(fileName, "r")
    # create new file to write out to
    scrambledFile = open("ScrambledFile.txt", "w+")
    scrambledFile.writelines("Cora Pohlman\n")
    scrambledFile.writelines("Word Scramble\n")
    scrambledFile.writelines("Program by Kate Pohlman\n")
    scrambledFile.writelines(str(date.today().strftime("%B %d, %Y")))
    scrambledFile.writelines("\n\n\n")

    words = []

    a = True

    while a:
        word = textFile.readline()
        if not word:
            a = False
            break
        words.append(word)

    # randomly rearrange elements in array
    random.shuffle(words)
    count = 0
    for x in words:
        x = scramble(x)
        count += 1
        scrambledFile.writelines((str(count) + ".  " + format(x, "12s")))
        scrambledFile.writelines("   ___________________________________________")
        scrambledFile.writelines("\n\n\n")

    textFile.close()
    scrambledFile.close()


main()
