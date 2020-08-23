sisse = open("sisseränne.txt", encoding="UTF-8")
valja = open("väljaränne.txt",encoding="UTF-8")
sisseränne = []
väljaränne = []
rände = []
for rida in sisse:
    sisseränne.append(int(rida.rstrip('\n')))

for rida in valja:
    väljaränne.append(int(rida.rstrip('\n')))
    

sisse.close()
valja.close()

for x in range(0,len(sisseränne)):
    vahe = sisseränne[x]-väljaränne[x]
    rände.append(vahe)

print(rände)
pos = max(rände)
if pos<=0:
    print("Positiivse rändesaldoga aastaid ei ole.")
else:
    print(rände.index(pos)+1)