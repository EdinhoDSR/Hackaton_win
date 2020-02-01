from tika import parser
import os

def simpifierCV(textCV):
    textCV = textCV['content'].split("\n\n")
    chaine = []
    for i in textCV:
        len = sum(j.isalpha() for j in i )
        if 1 < len and len < 50 and i[0].isupper():
            chaine += i
    return chaine

for element in os.listdir(r'C:\Users/augus/PycharmProjects/hackathon/CVs'):
    parsed = parser.from_file(r'C:\Users/augus/PycharmProjects/hackathon/CVs/' + element)
    print(simpifierCV(parsed))











