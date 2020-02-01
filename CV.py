# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:14:01 2020

@author: Yakiimo
"""

from tika import parser
raw = parser.from_file('1Amy.pdf')
print(raw['content'])
print("\n\n")
text = raw['content'].lower().split()

excludedWords = ["or", "and", "with", "from", "of"]
wordsCount = {}

def scanCV(text) :
    for word in text :
        if word in wordsCount.keys() :
            wordsCount[word]+=1
        else :
            wordsCount[word]=0
            
scanCV(text)
print(wordsCount)