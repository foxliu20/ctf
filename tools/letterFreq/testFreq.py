#!/usr/bin/env python3

# Letter Frequency Statistical Decryption
# Author : FoX
# Date : 2017-02-04

def letterFreqDict():
    engLetterFreqDict = {
            'E' : 0.1268, 'T' : 0.0978, 'A' : 0.0788, 'O' : 0.0776, 'I' : 0.0707, 'N' : 0.0706,
            'S' : 0.0634, 'R' : 0.0594, 'H' : 0.0573, 'L' : 0.0394, 'D' : 0.0389, 'U' : 0.0280,
            'C' : 0.0268, 'F' : 0.0256, 'M' : 0.0244, 'W' : 0.0214, 'Y' : 0.0202, 'G' : 0.0187,
            'P' : 0.0186, 'B' : 0.0156, 'V' : 0.0102, 'K' : 0.0060, 'X' : 0.0016, 'J' : 0.0010,
            'Q' : 0.0009, 'Z' : 0.0006
            }
    sortedList = sorted(engLetterFreqDict.items(), key=lambda x:x[1], reverse=True)
    letterByFreqDesc = next( zip(*sortedList) )
    return letterByFreqDesc

def countLetter(txt):
    counter = {}
    for i in range(26):
        counter[ chr(ord('A')+i) ] = 0

    for c in txt:
        if not c.isalpha():
            continue
        counter[ c.upper() ] += 1

    sortedList = sorted(counter.items(), key=lambda x:x[1], reverse=True)
    letterByCountDesc = next( zip(*sortedList) )
    return letterByCountDesc

def main():
    txt = input()
    engLetters = "".join( letterFreqDict() )
    txtLetters = "".join( countLetter(txt) )

    engLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    txtLetters = "QAZWSXEDCRFVTGBYHNUJMIKOLP"

    trantab = str.maketrans(txtLetters + txtLetters.lower(), engLetters + engLetters.lower())
    print( txt.translate(trantab) )

if '__main__' == __name__:
    main()
