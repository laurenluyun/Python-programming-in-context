# -*- coding = utf-8 -*-
# @Time : 5/22/2023 10:35 AM
# @Author : Lauren
# @File : railFence.py
# @Software : PyCharm
'''
Cracking the rail fence
ProblemL there is no "wordlist.txt"
'''


def railDecrypt(cipherText, numRails):
    '''
    the method helps to find the first six characters in the decrypted
    message, by translating the coordinates for data stored in tabular form
    into linear form.
    '''
    # numRails are the number of rows in the text if numRails = 3, railLen
    # = 6, rail = row, below is row-major order
    railLen = len(cipherText) // numRails
    solution = ''
    # iterate through each col, range(0, 6)
    for col in range(railLen):
        # iterate through each element of each col, range(0, 3)
        for rail in range(numRails):
            # translate the index into the one-dimensional string3
            # index at 0, 6, 12, 1...=> the 1st, 7th, 13th, 2nd element of
            # the string
            nextLetter = col + (rail * railLen)
            # concatenate the char by the order above
            solution += cipherText(nextLetter)
    # return the solution in list
    return solution.split()

def createWordDict(dName):
    myDict = {}
    with open(dName, 'r') as myFile:
        for line in myFile:
            # slice operation that extracts all characters from line except
            # the last one. It effectively removes the last character from the string.
            # set all values to True
            myDict[line[:-1]] = True
    return myDict

def railBreak(cipherText):
    wordDict = createWordDict("wordlist.txt")
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No word found in dictionary" #default response
    for i in range(2, cipherLen + 1):
        words = railDecrypt(cipherText, i)
        goodCount = 0 # reset for new list
        for w in words:
            # if a word is in the dictionary of known words, we increment
            # the goodCount by 1
            if w in wordDict:
                goodCount += 1
        # we use the min-max pattern. When the current decrypted word list
        # contains more known words than any of the previous decryptions,
        # we remember it by setting maxGoodSoFar
        if goodCount > maxGoodSoFar: # if more words in this list
            maxGoodSoFar = goodCount
            # we remember the best version of the message so far by
            # assigning it the name bestGuess
            bestGuess = " ".join(words) # join words in list with space
    return bestGuess

def main():
    cipherText = "n aci mreidontoowp mgorw"
    print(railBreak(cipherText))

if __name__ == "__main__":
    main()