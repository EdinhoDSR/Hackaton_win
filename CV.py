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

def countCV(dirs) :
    count = 0
    for file in dirs :
        if "pdf" in file :
            count += 1
    return count

def scanCV(dirs) :
    '''Scanne les fichiers et enregistre dans un dictionnaire chacun des mots et leurs nombres d'apparition'''
    for file in dirs :
        if "pdf" in file :     
            raw = parser.from_file(path + "\\" + file)
            text = raw['content'].lower().split()
            countWords(text)

def countWords(text) :
    '''Ajoute 1 a la valeur de la cle correspondante dans le dictionnaire ou cree la cle si inexistante'''
    for word in text :
        if word in wordsCount.keys() :
            wordsCount[word]+=1
        else :
            wordsCount[word]=1
            
def updateKeyWords() :
    '''Met a jour la liste des mots cles s'ils sont apparus plus d'une fois et n'appartiennent pas a la liste des mots a exclure'''
    for word in wordsCount.keys() :
        if wordsCount[word] >= 10 and not word in excludedWords :
            keyWords[word] = [wordsCount[word]]
            
def displayWordsOccurrences() :
    '''Affiche les mots tries selon leurs nombres d'apparition'''
    for word in sorted(wordsCount, key=wordsCount.get, reverse=True):
        if wordsCount[word] >= 10 and not word in excludedWords :
            print(word, wordsCount[word])
            
def importance(text):
    '''Calcule le score d'un CV en fonction des mots trouves a l'interieur'''
    score=0
    for word in keyWords.keys(): #pour chaque mot du dico des mots-cles, recuperer l'occurrrence dans le cv, le multiplier par ln(la valeur) et ajouter à la note
        if keyWords.get(word,0)[0] == 0 or text.count(word) == 0:
            continue
        score = score + math.log(text.count(word)*keyWords.get(word,0)[0])
    return score

def getScores(dirs):
    '''Calcule les scores de tous les CV'''
    scores = {}
    for file in dirs :
        if "pdf" in file :     
            raw = parser.from_file(path + "\\" + file)
            text = raw['content'].lower().split()
            scores[file] = importance(text)
    for file in sorted(scores, key=scores.get, reverse=True):
        print(file + "\t\t" + str(scores[file]))
    
            
scanCV(dirs)
# print(wordsCount)
updateKeyWords()
print(keyWords)
# displayWordsOccurrences()
getScores(dirs)

