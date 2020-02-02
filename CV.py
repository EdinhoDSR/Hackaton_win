# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:14:01 2020

@author: Yakiimo
"""

import os
import math
from tika import parser
from tkinter import *
path = r"C:\Users\Yakiimo\Desktop\Hackathon CV\CV\Resume&Job_Description\Original_Resumes"
dirs = os.listdir(path)

excludedWords = ["or", "and", "with", "from", "of", "any", "to", "for", "-", "by", 
                 "which", "as", "in", "on", "to", "–", "•", ":", "&", "a", ",", "an", 
                 "the", "then", "cvs", "we", "at","is", "are", "that", "be", "can", "this",
                 "it", "our", "all", "", "etc.", "ltd"]
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
            keyWords[word] = 0
            
def displayWordsOccurrences() :
    '''Affiche les mots tries selon leurs nombres d'apparition'''
    for word in sorted(wordsCount, key=wordsCount.get, reverse=True):
        if wordsCount[word] >= 10 and not word in excludedWords :
            print(word, wordsCount[word])
            
def importance(text):
    '''Calcule le score d'un CV en fonction des mots trouves a l'interieur'''
    score=0
    for word in keyWords.keys(): #pour chaque mot du dico des mots-cles, recuperer l'occurrrence dans le cv, le multiplier par ln(la valeur) et ajouter à la note
        if keyWords.get(word,0) == 0 or text.count(word) == 0:
            continue
        score = score + math.log(text.count(word)*keyWords.get(word,0))
    return score

def getScores(dirs):
    '''Calcule les scores de tous les CV'''
    scores = {}
    for file in dirs :
        if "pdf" in file :     
            raw = parser.from_file(path + "\\" + file)
            text = raw['content'].lower().split()
            scores[file] = importance(text)
    return scores

def getCVName(dirs) :
    '''Calcule les scores de tous les CV'''
    cvList  = []
    for file in dirs :
        if "pdf" in file : 
            cvList.append(file)
    return cvList
    
            
scanCV(dirs)
# print(wordsCount)
updateKeyWords()
print(keyWords)
# displayWordsOccurrences()
scores = getScores(dirs)
for file in sorted(scores, key=scores.get, reverse=True):
        print(file + "\t\t" + str(scores[file]))


fenetre = Tk()
fenetre.geometry("")

titre = Label(fenetre, text = "Gestion des CVs", font=("Helvetica", "24", "bold"))
titre.grid(row = 0, column = 8, pady = 10, columnspan = 3)


def asset_cvs() :
    scores = getScores(dirs)
    for file in sorted(scores, key=scores.get, reverse=True):
        print(file + "\t\t" + str(scores[file]))
    message['text'] = "CVs évalués !"
    fenetre.after(1000, clear_message)
        
        
evalCV = Button(fenetre, text = "Évaluer des CVs", command = asset_cvs, font=("Helvetica", "16", "bold"))
evalCV.grid(row=3, column= 8, pady = 10, columnspan = 3)

'''
scales_dict = {}

for word in keyWords :
    scales_dict[word]= Scale(fenetre, orient='horizontal', from_=0, to=10, resolution=0.1, tickinterval=2, length=350, label=word)
'''

keyWordsKeys = list(keyWords.keys())
scales = []
j = 0

for i in range (len(keyWords)) :
    if i%9 == 0 :
        j+=1
    scale = Scale(fenetre, from_=0, to = 100, label = keyWordsKeys[i], orient='horizontal', font=("Helvetica", "12"))
    scale.grid(row = 4+i%8, column = 4+j, padx = 10, pady = 5)
    scales.append(scale)
    
def change_scales() :
    for i in range (len(keyWords)) :
       keyWords[keyWordsKeys[i]] = scales[i].get()
    print(keyWords)
    message['text'] = "Coefficients modifiés !"
    fenetre.after(1000, clear_message)
    
def clear_message() :
    message["text"] = ""
        
submitScale = Button(fenetre, text="Valider", command=change_scales, font=("Helvetica", "16", "bold"))
submitScale.grid(row = 18, column = 8, pady = 20, columnspan = 3)

message = Label(fenetre, text="", font=("Helvetica", "16", "bold"))
message.grid(row = 20, column = 8, columnspan = 3, pady = 10)

scoreLabels = []
r = 0
for file in getCVName(dirs) :
    scoreLabel = Label(fenetre, text= file + "\t\t" + str(scores[file]), font=("Helvetica", "12"))
    scoreLabel.grid(row = r, column = 15, padx = 10, pady = 5)
    scoreLabels.append(scoreLabel)
    r+=1


'''
for word in scales_dict :
    def changeCoefficient() :
        keyWords[word] = scales_dict[word].get()
        print(word)
        print(keyWords[word])
        print(scales_dict[word].get())
        print(keyWords[word])
    scales_dict[word].config(command=changeCoefficient)
    scales_dict[word].grid(row = 2, column = 2)
'''
    


fenetre.mainloop()

