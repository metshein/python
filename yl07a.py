# 22.10.24 Metshein
# Ülesanded 7 Loendid
import datetime

# Tänane kuu number
x = datetime.datetime.now()
tana = int(x.strftime("%m")) - 1 # -1 et loendiga ühildada

# 12 kuud
kuud = [["jaanuar",27,8,26,26,-13,17,-2,22,20,5,-9,-9,-12,1,-3,11,-15,28,29,-3,14,-1,-17,-18,4,-8,-16,3,7,2,30],
["veebruar",-15,11,24,11,-6,-11,0,20,-14,20,22,17,5,15,-1,-4,22,-4,-4,18,-19,2,13,-7,-13,12,-5,8],
["märts",-11,-15,23,26,4,-4,29,1,9,17,3,19,-7,-17,23,9,28,4,26,20,-9,2,12,-14,-2,-12,19,17,26,-4,-1],
["aprill",6,-10,-18,15,14,15,27,-16,-10,-13,4,23,-5,9,-4,21,26,15,-15,11,10,27,-14,24,14,14,-16,-5,-5,9],
["mai",-15,28,19,4,-20,16,-4,-15,-5,6,8,19,-9,26,-9,-16,-1,30,4,15,1,0,23,21,3,20,1,17,11,21,-16],
["juuni",-7,0,-9,-8,-17,13,-20,-6,-3,-16,19,-12,-14,27,29,-15,27,21,-1,22,-2,12,19,-2,-12,15,8,-13,0,29],
["juuli",2,-2,20,12,-20,16,25,-9,24,7,3,19,3,-10,27,-7,-2,13,3,27,-7,25,-13,27,26,-20,29,15,26,10,-20],
["august",2,24,11,22,6,0,-2,-14,-5,13,-17,-14,-5,20,-11,12,14,-1,23,-14,28,24,-10,-16,-10,-4,26,25,-1,18,-5],
["september",3,-20,30,22,25,-5,12,14,-13,2,20,15,25,16,-15,26,0,12,-19,-5,-5,4,-15,-4,3,8,5,-9,-4,-10],
["oktoober",1,-19,26,-17,2,27,13,16,-6,22,-7,10,12,18,-8,-1,14,18,1,-19,11,18,2,27,-18,27,15,-7,-9,21,-12],
["november",-8,9,-15,-7,9,6,0,9,30,-18,20,-10,27,-18,21,30,11,-4,25,27,14,7,13,22,24,15,13,-6,11,2],
["detsember",9,-6,7,4,-5,-8,14,19,13,29,-15,-3,-8,23,-10,-11,25,-15,1,21,17,-14,19,-4,18,12,-1,18,16,-5,-10]]

#Ülesanded
print(kuud[tana][0])
print(f"Viimane mõõtmine sellel kuul: {kuud[tana][len(kuud[tana])-1]}")
ajutine = []
for i in range(len(kuud[tana])-1):
    ajutine.append(kuud[tana][i+1])
    print(kuud[tana][i+1], end=", ")

print()
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")

print(f"-20 esineb {ajutine.count(-20)} korda")

ajutine.pop(5)
print(ajutine)





"""
# Jukebox
muusika = ['ALIKA – "Bridges"',
'Anett x Fredi – "Read Between The Lines"',
'villemdrillem – "leekiv armastus"',
'Clicherik & Mäx – "PAKSUD"',
'nublu – "ära ärata"',
'NOËP – "Move Your Feet"',
'Trad.Attack! – "Bring It On"',
'Bedwetters – "It Is What It Is"',
'Reket – "Panama paberid"',
'Grete Paia – "Võluväel"']

for i in range(len(muusika)):
    print(str(i+1)+". "+muusika[i])

try:
    valik = int(input("Vali laul: "))
    print(f"Mängin lugu {muusika[valik-1]}")
except:
    print("Midagi läks katki. Teavita adminni")


"""