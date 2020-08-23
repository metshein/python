# Iseseseisev projekt
# Eesmärk: Firma tegeleb puidust nimepusledega, kus ühe tähe hind on 2€.
# Kasutaja esitab tekstifaili nimedaga (ülevalt alla) ning programm arvutab iga nimepusle hinna, käibemaksu ja kogusumma.
# Summad ümardatakse kahe komakohani ning väljastab tulemuse koos nimega ekraanile. Programm sisaldab ka faili kontrolli.
#Mark Metshein
## kommenteeritud
## vähemalt 1 funktsioon
## vähemalt 1 tingimuslause
## vähemalt 1 tsükkel
## kasutajalt küsida andmeid
## väljund ekraanil või faili
## kasuta järjendit

#filepath moodul 
import os.path
from os import path

#muutujad
hind = 2
koik_kokku = 0
km = 0.2
tellimus = []

#funktsioon nimede töötluseks
def pusle_hind(nimi, hind):
    '''Arvutab nimepuslede hinnad'''
    puhNimi = nimi.strip().upper()
    kokku = len(nimi)
    summa = kokku * hind
    return [puhNimi,kokku,summa]


#Erind veatete loomiseks
try:
    #Faili valimine ja kontroll
    failinimi = input("Sisesta faili nimi: ")
    if path.isfile(failinimi):
        fail = open(failinimi, encoding="UTF-8")
    else:
        print("Sellist faili pole!")
    
    #faili sisu tellimustele lisamine ja kogusumma arvutamine
    for rida in fail:
        vastus = pusle_hind(rida, hind)
        tellimus.append(vastus)
        koik_kokku += vastus[2]
    
    #arve kuvamine koos vormingutega
    print("--------- ARVE ---------")
    print("Nimesid kokku: {}".format(len(tellimus)))
    print("Ühe tähe hind: {:.2f}€".format(hind))
    for i in tellimus:
        print('{} {}tk {}€'.format(*i))
    print("Käibemaks: {:.2f}€".format(koik_kokku*km))
    print("-----------------\nKuulub tasumisele: {}€".format(koik_kokku+koik_kokku*km))
except:
  print("Arvet ei loodud!") 

