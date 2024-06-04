# -*- coding = utf-8 -*-
# @Time : 4/29/2023 12:29 PM
# @Author : Lauren
# @File : Mapping.py
# @Software : PyCharm

def letterToIndex(letter):
    from string import ascii_lowercase
    # abcdefghijklmnopqrstuvwxyz with space at the end as the 27th letter
    alphabet = ascii_lowercase + ' '
    index = alphabet.find(letter.lower())
    if index == -1:
        print("error:", letter, "is not in the alphabet.")
    else:
        print(index)

def indexToLetter(index):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    if index >= len(alphabet):
        print("error:", index, "is too large.")
    elif index < 0:
        print("error:", index, "is less than 0.")
    else:
        print(alphabet[index])

def main():
    letter_1 = 'a'
    letter_2 = '1'
    letter_3 = ' '
    letterToIndex(letter_1)
    letterToIndex(letter_2)
    letterToIndex(letter_3)
    print("======================")
    index_1 = 0
    index_2 = 26
    index_3 = -1
    index_4 = 27
    indexToLetter(index_1)
    indexToLetter(index_2)
    indexToLetter(index_3)
    indexToLetter(index_4)

if __name__ == "__main__":
    main()