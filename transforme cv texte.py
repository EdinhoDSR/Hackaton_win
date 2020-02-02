# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import os
from tika import parser
parsed = parser.from_file(r"CV\Resume&Job_Description\Original_Resumes\1Amy.pdf")
print(type(parsed))
print(type(parsed["content"]))

x = parsed["content"].split()
print(x)
print(x.count("AMY"))
def importance(dico):
    for clé in dico.keys:
        dico.count(clé)
#for element in parsed["content"]:
#    print(element)
#print(parsed["content"][0:50])
"""
for element in os.listdir('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Administration/CDIB HK - Office Manager') :
    parsed = tika.parser.from_file('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Administration/CDIB HK - Office Manager/' + element)
    print(parsed["content"])
"""
#help("parser")