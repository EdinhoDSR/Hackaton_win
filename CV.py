# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:14:01 2020

@author: Yakiimo
"""

import os
import csv
from tika import parser
path = r"C:\Users\Yakiimo\Desktop\Hackathon CV\CV\Resume&Job_Description\Original_Resumes"
dirs = os.listdir(path)

excludedWords = ["or", "and", "with", "from", "of", "any", "to", "for", "-", "by", "which", "as", "in", "on", "to", "–", "•", ":", "&"]
keyWords = {}
wordsCount = {}

def scanCV(dirs) :
    for file in dirs :
        if "pdf" in file :     
            raw = parser.from_file(r"C:\Users\Yakiimo\Desktop\Hackathon CV\CV\Resume&Job_Description\Original_Resumes\\"+file)
            print(raw['content'])
            print("\n\n")
            text = raw['content'].lower().split()
            countWords(text)

def countWords(text) :
    for word in text :
        if word in wordsCount.keys() :
            wordsCount[word]+=1
        else :
            wordsCount[word]=0
            
def updateKeyWords() :
    for word in wordsCount.keys() :
        if wordsCount[word] >= 30 and not word in excludedWords :
            keyWords[word] = []
            
scanCV(dirs)
print(wordsCount)
updateKeyWords()
print(keyWords)

