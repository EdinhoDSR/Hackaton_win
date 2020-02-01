# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:14:01 2020

@author: Yakiimo
"""

import os
import math
from tika import parser
path = r"C:\Users\Yakiimo\Desktop\Hackathon CV\CV\Resume&Job_Description\Original_Resumes"
dirs = os.listdir(path)

excludedWords = ["or", "and", "with", "from", "of", "any", "to", "for", "-", "by", 
                 "which", "as", "in", "on", "to", "–", "•", ":", "&", "a", ",", "an", 
                 "the", "then", "cvs", "we", "at","is", "are", "that", "be", "can", "this",
                 "it", "our", "all", ""]
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
            wordsCount[word]=1
            
def updateKeyWords() :
    for word in wordsCount.keys() :
        if wordsCount[word] >= 10 and not word in excludedWords :
            keyWords[word] = [wordsCount[word]]
            
def displayWordsOccurrences() :
    for word in sorted(wordsCount, key=wordsCount.get, reverse=True):
        if wordsCount[word] > 10 and not word in excludedWords :
            print(word, wordsCount[word])
            
def importance(words,CV):
    score=0
    parsed = parser.from_file(CV)
    CV_coupe = parsed["content"].split()
    for word in words.keys(): #pour chaque mots du dico des mots-clés, recuperer l'occurrrence dans le cv, le multiplier par ln(la valeur) et ajouter à la note
        if words.get(word,0)[0] == 0 or CV_coupe.count(word) ==0:
            continue
        score = score + math.log(CV_coupe.count(word)*words.get(word,0)[0])
    return score

            
scanCV(dirs)
print(wordsCount)
updateKeyWords()
print(keyWords)
displayWordsOccurrences()

