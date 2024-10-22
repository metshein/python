# 22.10.24 Metshein
# Ülesanne 7 Massiivid

# Aastaajad
kuud = [('jaanuar',3,-16,-16,-1,-7,9,-3,-13,8,9,3,7,9,0,-9,-10,-9,-11,-6,-10,-20,-20,-5,-14,9,-1,-10,-20,-12,7,-15),
('veebruar',8,8,0,-9,-16,-13,6,0,9,8,-3,-20,-17,5,-7,-5,-1,-10,-13,-19,-18,1,-8,-17,-19,-1,1,-6),
('märts',8,-15,10,7,1,-11,1,-14,2,10,-15,5,2,-11,-3,10,-9,-13,-10,8,10,9,10,-7,-19,-1,1,-10,-6,-1,-18),
('aprill',-3,-16,-7,2,-7,-12,-18,-5,-10,-14,-17,-14,3,-4,-2,-14,-20,-3,-1,9,-10,-19,8,-12,2,-12,-12,-7,-8,-7),
('mai',-17,-19,7,-13,-14,0,10,-17,10,-15,-8,1,-2,0,-12,-8,-14,-16,-4,-3,6,-9,-15,-12,10,-9,2,-15,-20,6,0),
('juuni',15,13,17,11,27,21,19,10,22,12,14,10,17,19,20,27,18,11,21,25,24,13,29,27,12,13,28,18,12,28),
('juuli',25,11,19,27,15,26,10,27,22,22,21,28,30,23,24,21,22,16,10,27,29,25,27,17,10,30,17,28,29,24,28),
('august',26,25,10,15,14,10,17,11,25,29,17,27,19,20,10,13,19,27,11,12,16,20,25,12,30,10,24,13,19,30,22),
('september',11,18,14,11,11,29,30,14,15,19,17,20,24,25,15,21,18,25,17,25,23,27,16,23,26,11,15,13,27,26),
('oktoober',-7,10,-1,1,0,-10,5,-11,-19,-1,-19,-11,-8,-4,-19,4,-16,2,-1,-18,-17,-8,6,4,5,-17,6,7,1,3,-10),
('november',-10,-19,-17,0,9,-10,-2,-2,-17,-8,-16,-18,2,10,-10,-7,-6,2,-3,-20,0,1,-9,-9,-6,0,-4,-16,-12,-7),
('detsember',9,-18,-7,-19,7,-11,-6,-14,-6,-5,-5,9,-7,-18,6,-13,-6,9,9,-11,-9,-3,-3,-11,-3,-11,4,6,-5,7,-2)]

print(f"Hetkekuu {kuud[9][0]}")
kuus_kokku = len(kuud[9])-1
print(f"Viimane mõõtmine: {kuud[9][kuus_kokku]}")
print("Selle kuu temperatuurid:")
ajutine = []
for i in range(kuus_kokku):
    ajutine.append(kuud[9][i+1])
    print(kuud[9][i+1], end=", ")
print()
print(f"Max temp: {max(ajutine)}")
print(f"Min temp: {min(ajutine)}")
print(f"Keskmine temp: {round(sum(ajutine)/len(ajutine),2)}")
print(f"-20 esineb {ajutine.count(-20)} korda")

ajutine.pop(5-1)
#del ajutine[4]
ajutine.insert(5-1,43)
ajutine.sort()
print(ajutine)




"""
# Muusikapalad
laulud = ['ALIKA – "Bridges"','Anett x Fredi – "Read Between The Lines"','villemdrillem – "leekiv armastus"','Clicherik & Mäx – "PAKSUD"','nublu – "ära ärata"','NOËP – "Move Your Feet"','Trad.Attack! – "Bring It On"','Bedwetters – "It Is What It Is"','Reket – "Panama paberid"','Grete Paia – "Võluväel"']


for i in range(10):
    print(str(i+1)+". "+laulud[i])
try:
    valik = int(input("Vali lugu 1-10: "))
    print(f"Mängin: {laulud[valik-1]}")
except:
    print("Tegid vale otsuse :)")

    """