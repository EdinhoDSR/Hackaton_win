# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:14:01 2020
@author: Yakiimo
"""

import os
import math
from tika import parser
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror

global path
global mostImportantKeyWords

excludedWords = ["or", "and", "with", "from", "of", "any", "to", "for", "-", "by", 
                 "which", "as", "in", "on", "to", "–", "•", ":", "&", "a", ",", "an", 
                 "the", "then", "cvs", "we", "at","is", "are", "that", "be", "can", "this",
                 "it", "our", "all", "", "etc.", "ltd", "pte", "|", "mar",""]
keyWords = {}
wordsCount = {}
def asset_cvs() :
    global path
    scores = getRealScores(os.listdir(path))
    scoresKeys = sorted(scores, key=scores.get, reverse=True)
    for i in range (len(scoresKeys)) :
        scoreLabels[i].config(text = scoresKeys[i] + "    " + str(scores[scoresKeys[i]]))
    augustin()

        
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

    

    updateKeyWords()

    valeurMax = 1

    for poids in keyWords.values() :

        if poids > valeurMax :

            valeurMax = poids

    print(valeurMax)        

    for word in wordsCount.keys() :

       wordsCount[word] = (wordsCount[word]/valeurMax)*100

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

            keyWords[word] = wordsCount[word]
            
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
        score = score + math.log(text.count(word)*keyWords.get(word))
    return score

def highImportance(text):
    '''Calcule le score d'un CV en fonction des mots trouves a l'interieur'''
    score=0
    for word in mostImportantKeyWords.keys(): #pour chaque mot du dico des mots-cles, recuperer l'occurrrence dans le cv, le multiplier par ln(la valeur) et ajouter à la note
        if mostImportantKeyWords.get(word,0) == 0 or text.count(word) == 0:
            continue
        
        score = score + math.log(text.count(word)*float(mostImportantKeyWords.get(word,0))+1)
    return score

def getScores(dirs):
    '''Calcule les scores de tous les CV'''
    scores = {}
    for file in dirs :
        if "pdf" in file :     
            raw = parser.from_file(path + "/" + file)
            text = raw['content'].lower().split()
            scores[file] = importance(text)
    return scores

def getRealScores(dirs):
    '''Calcule les scores de tous les CV'''
    scores = {}
    for file in dirs :
        if "pdf" in file :     
            raw = parser.from_file(path + "/" + file)
            text = raw['content'].lower().split()
            scores[file] = highImportance(text)
    return scores

def getCVName(dirs) :
    '''Calcule les scores de tous les CV'''
    cvList  = []
    for file in dirs :
        if "pdf" in file : 
            cvList.append(file)
    return cvList
    
def getMostImportantKeyWords() :
    mostImportantKeyWords = {}
    temp = sorted(wordsCount, key=wordsCount.get, reverse=True)
    i = 0
    for key in temp :
        if key not in excludedWords :
            mostImportantKeyWords[key] = wordsCount[key]
            i+=1
            if i == 10 :
                break
    return mostImportantKeyWords
  
'''            
scanCV(dirs)
# print(wordsCount)
updateKeyWords()
mostImportantKeyWords=getMostImportantKeyWords()
print(mostImportantKeyWords)
# displayWordsOccurrences()
scores = getScores(dirs)
for file in sorted(scores, key=scores.get, reverse=True):
        print(file + "\t\t" + str(scores[file]))

'''
'''
fenetre = Tk()
fenetre.geometry("")

menu = Frame(fenetre)
menu.grid(row = 0, column = 1, rowspan = 8, padx = 20)

titre = Label(menu, text = "Gestion des CVs", font=("Helvetica", "24", "bold"))
titre.grid(row = 0, column = 0, pady = 10, columnspan = 3)


def asset_cvs() :
    scores = getRealScores(dirs)
    scoresKeys = list(scores.keys())
    for i in range (len(scoresKeys)) :
        scoreLabels[i].config(text = scoresKeys[i] + "    " + str(scores[scoresKeys[i]]))
    message['text'] = "CVs évalués !"
    fenetre.after(1000, clear_message)
        
        
evalCV = Button(menu, text = "Évaluer des CVs", command = asset_cvs, font=("Helvetica", "16", "bold"))
evalCV.grid(row=2, column= 0, pady = 10, columnspan = 3)


scales_dict = {}
for word in keyWords :
    scales_dict[word]= Scale(fenetre, orient='horizontal', from_=0, to=10, resolution=0.1, tickinterval=2, length=350, label=word)


mostImportantKeyWordsKeys = list(mostImportantKeyWords.keys())
scales = []
deleteButtons = []
lines = []
j = 0

for i in range (len(mostImportantKeyWords)) :
    line = Frame(fenetre,borderwidth=1)
    label = Label(line, text = mostImportantKeyWordsKeys[i], font=("Helvetica", "12"))
    label.pack()
    scale = Scale(line, from_=0, to = 100, orient='horizontal')
    scale.set(mostImportantKeyWords[mostImportantKeyWordsKeys[i]])
    scale.pack()
    def deleteLine(i) :
        del mostImportantKeyWords[mostImportantKeyWordsKeys[i]]
        print(mostImportantKeyWords)
        scales[i].destroy
        print(scales.pop(i))
        lines[i].destroy
        print(lines.pop(i))
    deleteButton = Button(line, text = "X", command = lambda i=i: deleteLine(i), fg = "red")
    deleteButton.pack()
    lines.append(line)
    line.grid(row = i, column = 0)
    scales.append(scale)
    deleteButtons.append(deleteButton)
    
def change_scales() :
    for i in range (len(mostImportantKeyWords)) :
       mostImportantKeyWords[mostImportantKeyWordsKeys[i]] = scales[i].get()
    print(mostImportantKeyWords)
    message['text'] = "Coefficients modifiés !"
    fenetre.after(1000, clear_message)
    
def clear_message() :
    message["text"] = ""
        
submitScale = Button(menu, text="Valider", command=change_scales, font=("Helvetica", "16", "bold"))
submitScale.grid(row = 4, column = 0, pady = 20, columnspan=3)

message = Label(menu, text="", font=("Helvetica", "16", "bold"))
message.grid(row = 6, column = 0, columnspan = 3, pady = 10)

scoreLabels = []
r = 7
for file in getCVName(dirs) :
    scoreLabel = Label(menu, text = "", font=("Helvetica", "12"))
    scoreLabel.grid(row = r, column = 3, padx = 10, pady = 5)
    scoreLabels.append(scoreLabel)
    r+=1
    
# text= file + " " + str(scores[file])



for word in scales_dict :
    def changeCoefficient() :
        keyWords[word] = scales_dict[word].get()
        print(word)
        print(keyWords[word])
        print(scales_dict[word].get())
        print(keyWords[word])
    scales_dict[word].config(command=changeCoefficient)
    scales_dict[word].grid(row = 2, column = 2)

    


fenetre.mainloop()
'''

global nbCoeffs
global tableau
nbCoeffs = 10
mostImportantKeyWords = {}

def afficherCoefficient(frame,string,double,i):
    global mostImportantKeyWords
    if string not in mostImportantKeyWords:
        mostImportantKeyWords[string] = double
    ligne = Frame(frame,borderwidth=1)
    labelMot=Label(ligne,text=string)
    labelMot.grid(row=i,column=0,padx=5,sticky=E)        
    scale = Scale(ligne,orient='horizontal',from_=0,to=100,resolution=0.1,length=150,command= lambda i=2,nom=string : actualiser(nom,i))
    scale.set(double)
    scale.grid(row=i,column=1,padx=20,pady=1)
    boutonSupprimer = Button(ligne, text="X",command= lambda : destruction(ligne,string))
    boutonSupprimer.grid(row=i,column=2,padx=5,pady=2)
    ligne.pack()

def actualiser(nom,valeur):
    global mostImportantKeyWords
    print(nom,valeur)
    mostImportantKeyWords[nom] = valeur
def destruction(ligne,nom):
    del mostImportantKeyWords[nom]
    print(mostImportantKeyWords)
    ligne.destroy()
def demanderPath():
    global path
    global scoreLabels
    path = askdirectory()
    labelPath.config(text=path)
    r = 7
    for file in getCVName(os.listdir(path)) :
        scoreLabel = Label(mainCadreDroit, text = "", font=("Helvetica", "12"))
        scoreLabel.grid(row = r, column = 3, padx = 10, pady = 5)
        scoreLabels.append(scoreLabel)
        r+=1
    importerDico()
    return 
#entrer une donnée
def demanderNouveauMot():
    entree = Tk()
    value = StringVar()
    value.set("Ajouter un paramètre")
    valeur = Entry(entree, textvariable=value, width = 30)
    poids = DoubleVar()
    scale = Scale(entree, variable=poids,orient='horizontal',from_=0,to=100,resolution=0.1,label='Importance du mot-clé',length=250)
    scale.set(10)
    boutonAjouter = Button(entree, text="Ajouter",command=lambda : afficherCoefficient(tableau,valeur.get(),scale.get(),nbCoeffs))
    boutonAjouter.pack(side=RIGHT,padx=5,pady=30)
    valeur.pack(side=LEFT,padx=5,pady=30)
    scale.pack(padx=10)

    

        
fenetre = Tk()
fenetre.geometry("1000x700")
#colonne de gauche
mainCadreGauche = Frame(fenetre, borderwidth=1) #le cadre principal de gauche
mainCadreGauche.pack(side=LEFT,fill=Y)

label=Label(mainCadreGauche,text="Bienvenue dans votre gestionnaire de CV",font=("Helvetica", "24", "bold"))
label.pack(pady=2,side=TOP)


#ligne "parcourir"
lignePath = Frame(mainCadreGauche,borderwidth=1)
lignePath.pack(pady=0,fill=BOTH)
bouton=Button(lignePath, text="Parcourir",command=demanderPath)
bouton.pack(side=LEFT)
labelPath=Label(lignePath,text="Veuillez choisir le fichier dans lequel se trouve les CV")
labelPath.pack(padx=10)
defilement = Scrollbar(mainCadreGauche)
defilement.pack(side=LEFT, fill=Y)
canva = Canvas(mainCadreGauche,yscrollcommand=defilement.set)
canva.pack(fill='both', expand=True)
tableau = Frame(canva)
defilement.config(command=canva.yview)
window = canva.create_window(0,0, anchor=NW,window=tableau)
tableau.pack()




bouton=Button(mainCadreGauche, text="+",command=demanderNouveauMot)
bouton.pack(side=BOTTOM,padx=15)
evalCV = Button(mainCadreGauche, text = "Évaluer des CVs", command = asset_cvs, font=("Helvetica", "16", "bold"))
evalCV.pack(side=RIGHT)
mainCadreDroit = Frame(fenetre, width=768, height=576, borderwidth=1) #le cadre principal de droite
scoreLabels = []

mainCadreDroit.pack(side=RIGHT)


def importerDico():
    global tableau
    global mostImportantKeyWords
    j=0
    scanCV(os.listdir(path))
    updateKeyWords()
    mostImportantKeyWords=getMostImportantKeyWords()
    scores = getScores(os.listdir(path))
    for i in mostImportantKeyWords:
        afficherCoefficient(tableau,i,mostImportantKeyWords.get(i),j)
        j=j+1
    return True
def augustin():
    fenetre.destroy()


fenetre.mainloop()