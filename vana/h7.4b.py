from urllib.request import urlopen

kuu=input("Kuu: ")
paev = int(input("Päev: "))
failVeebis = urlopen("http://kodu.ut.ee/~eno/mooc/"+kuu)
baidid = failVeebis.read()
tekst = baidid.decode()            # baitidest saab sõne
ridadeKaupa = tekst.splitlines()   # sõne jaotatakse reavahetuse kohtadelt
failVeebis.close()
print(ridadeKaupa[paev-1])              # rida indeksiga 4


