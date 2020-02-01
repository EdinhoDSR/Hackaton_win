# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import os
import math
from tika import parser

def importance(dico,CV):
    
    note=0
    parsed = parser.from_file(CV)
    CV_coupe = parsed["content"].split()
    
    for cle in dico.keys(): #pour chaque mots du dico des mots-clés, recuperer l'occurrrence dans le cv, le multiplier par ln(la valeur) et ajouter à la note
        if dico.get(cle,0)[0] == 0 or CV_coupe.count(cle) ==0:
            continue
        note = note + math.log(CV_coupe.count(cle)*dico.get(cle,0)[0])
    return note 

#for element in parsed["content"]:
#    print(element)
#print(parsed["content"][0:50])
"""
for element in os.listdir('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Administration/CDIB HK - Office Manager') :
    parsed = tika.parser.from_file('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Administration/CDIB HK - Office Manager/' + element)
    print(parsed["content"])
"""
#help("parser")