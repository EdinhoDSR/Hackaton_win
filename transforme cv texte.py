# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import os
import tika
parsed = tika.parser.from_file('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Legal/Vistra SG - Legal Counsel/Duane Morris_Victoria Lee_Lawyer.pdf')
print(parsed["content"])
for element in os.listdir('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Administration/CDIB HK - Office Manager') :
    parsed = tika.parser.from_file('C:/Users/alexandre/Desktop/CV/Resume&Job_Description/Original_Resumes/Administration/CDIB HK - Office Manager/' + element)
    print(parsed["content"])
#help("parser")