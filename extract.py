from tika import parser
raw = parser.from_file('2Ben.pdf')
text = raw['content'].split(" ")
print(text)
chaine = str()
bool = True
for i in text:
    if i[:5] == '\n\n•':
        bool = False
    elif i[:4] == '\n\n':
        bool = True
    if bool:
        chaine += i
print(chaine)








