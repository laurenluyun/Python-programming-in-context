# -*- coding = utf-8 -*-
# @Time : 5/22/2023 2:24 PM
# @Author : Lauren
# @File : SubstitutionCipher.py
# @Software : PyCharm

def removeMatches(myString, removeString):
    '''
    This functions helps to remove the elements in the original string that
    are not needed, like space, punctuations
    '''
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr += ch
    return newStr

def letterFrequency(text):
    text = text.lower
    nonLetters = removeMatches(text, 'abcdefghijklmnopqrstuvwxyz')
    # update the text by removing all nonLetters
    text = removeMatches(text, nonLetters)
    lCount = {}
    total = len(text)
    # count each letter's occurrence
    for ch in text:
        # lCount.get(ch, 0) retrieves the current count of the character ch
        # from the dictionary lCount. If the character ch is not present in
        # the dictionary, it returns the default value of 0.
        lCount[ch] = lCount.get(ch, 0) + 1
    # then calculate percentage and update it in the lCount dict
    for ch in lCount:
        lCount[ch] = lCount[ch] / total
    return lCount

def getFreq(t):
    # return second item in the tuple
    return t[1]

def maybeAdd(ch, toDict):
    if ch in 'abcdefghijklmnopqrstuvwxyz':
        toDict[ch] = toDict.setdefault(ch, 0) + 1

def neighborCount(text):
    nbDict = {}
    text = text.lower()
    for i in range(len(text) - 1):
        # The setdefault method first checks whether the key is in
        # the dictionary. If it is not, it adds the default value and returns
        # a reference to the default value, which is then assigned to the
        # list of neighbors. T
        nbList = nbDict.setdefault(text[i], {})
        maybeAdd(text[i + 1], nbList)
        nbList = nbDict.setdefault(text[i + 1], {})
        maybeAdd(text[i], nbList)

    return nbDict

def sortByLen(w):
    return len(w)

cipherText = ''
cipherWords = cipherText.split()
cipherWords.sort(key = sortByLen)