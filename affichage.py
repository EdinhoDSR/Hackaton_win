# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
global path 
global nbCoeffs
path = "a"
nbCoeffs = 10

def afficherCoefficient(frame,string,double,i):
        ligne = Frame(frame,borderwidth=1)
        labelMot=Label(ligne,text=string)
        labelMot.grid(row=i,column=0,padx=5,sticky=E)        
        scale = Scale(ligne,orient='horizontal',from_=0,to=5,resolution=0.01,length=150)
        scale.set(double)
        scale.grid(row=i,column=1,padx=20,pady=20)
        boutonSupprimer = Button(ligne, text="X",command=ligne.destroy)
        boutonSupprimer.grid(row=i,column=2,padx=5,pady=30)
        ligne.pack()
    
def demanderPath():
    path = askdirectory()
    labelPath.config(text=path)
    return 
#entrer une donnée
def demanderNouveauMot():
    entree = Tk()
    value = StringVar()
    value.set("Ajouter un paramètre")
    valeur = Entry(entree, textvariable=value, width = 30)
    poids = DoubleVar()
    scale = Scale(entree, variable=poids,orient='horizontal',from_=0,to=5,resolution=0.01,label='Importance du mot-clé',length=250)
    scale.set(1)
    boutonAjouter = Button(entree, text="Ajouter",command=lambda : afficherCoefficient(mainCadreGauche,valeur.get(),scale.get(),nbCoeffs))
    boutonAjouter.pack(side=RIGHT,padx=5,pady=30)
    valeur.pack(side=LEFT,padx=5,pady=30)
    scale.pack(padx=10)

    

        
fenetre = Tk()
#colonne de gauche
mainCadreGauche = Frame(fenetre, width=768, height=576, borderwidth=1) #le cadre principal de gauche
mainCadreGauche.pack(side=LEFT)

label=Label(mainCadreGauche,text="Bienvenu dans votre gestionnaire de CV")
label.pack(pady=10)


#ligne "parcourir"
lignePath = Frame(mainCadreGauche,borderwidth=1)
lignePath.pack(pady=10,fill=BOTH)
bouton=Button(lignePath, text="Parcourir",command=demanderPath)
bouton.pack(side=LEFT)
labelPath=Label(lignePath,text="Veuillez choisir le fichier dans lequel se trouve les CV")
labelPath.pack(padx=10)

defilement = Scrollbar(mainCadreGauche)
defilement.pack(side=LEFT)
for i in range(nbCoeffs):
    afficherCoefficient(mainCadreGauche,"test",3,i)
bouton=Button(mainCadreGauche, text="+",command=demanderNouveauMot)
bouton.pack(side=BOTTOM,padx=15)

mainCadreDroit = Frame(fenetre, width=768, height=576, borderwidth=1) #le cadre principal de droite
mainCadreDroit.pack(side=RIGHT)
fenetre.mainloop()

