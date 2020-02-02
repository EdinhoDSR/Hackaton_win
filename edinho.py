# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import os
import math
from tika import parser

parsed = parser.from_file(r"CV\Resume&Job_Description\Original_Resumes\Addleshaw_Treliza Li_Office Manager.pdf")
CV_coupe = parsed["content"].split()
print(CV_coupe)
print(parsed["metadata"])


def importance(dico,CV):
    
    note=0
    parsed = parser.from_file(CV)
    CV_coupe = parsed["content"].split()
    
    for cle in dico.keys(): #pour chaque mots du dico des mots-clés, recuperer l'occurrrence dans le cv, le multiplier par ln(la valeur) et ajouter à la note
        if dico.get(cle,0)[0] == 0 or CV_coupe.count(cle) ==0:
            continue
        note = note + math.log(CV_coupe.count(cle)*dico.get(cle,0)[0])
    return note 



#help("parser")