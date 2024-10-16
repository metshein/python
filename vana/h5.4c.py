from datetime import *
valik = input("Vali fail (nimekiri.txt): ")
fail = open(valik, encoding="UTF-8")
nimed = []
for rida in fail:
    nimed.append(rida)
fail.close()

print(nimed[(datetime.now().day)-1],end="")