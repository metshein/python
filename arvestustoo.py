# ARVESTUSTÖÖ - Python
# PANE SIIA OMA NIMI
######## LOTOVÕIDUD ########
# Andmed inimeste lotovõitude kohta: nimi, perenimi, isikukood, elukoht, võitmise kuu ja võidetud summa.
# Iga isiku andmed (kirje) on eraldi reas (rea lõpus \n – reavahetussümbol). Ühe isiku andmeväljad on eraldatud ühe tühikuga.
# Lugeda andmed failist loendi(te)sse ning kirjutada päringute tulemusi uutesse failidesse.
# Väljastada read ja kirjutada neid ridu UUE FAILI -> iga päringu kohta uus fail, kus on:
#
#    isikute perenimed algavad tähega "P" - 5p
#    isikud, kes on sündinud kevadel - 5p
#    isikute elukohaks on linn Riga - 5p
#    isikute võidusumma on paarisarv - 5p
#    isikud, kes on mehed - 5p
#    isikud, kellel eesnimi ja perenimi tähed on samad - 5p
#
# Iga päringu kohta koostada eraldi funktsiooni, mille parameetriks võiks olla vastavalt:
#    täht
#    aastaaeg (näiteks stringi kujul "kevad" või "spring" siin kuidas otsustate)
#    linn
#    pole vaja parameetrit
#    sugu
#    täht


fail = "nimed.txt"

def algustäht(fail, täht="p"):
    '''Lisab teatud perenime algustähega read uude faili'''
    try:
        f = open(fail, encoding="UTF-8")
        fail_kirjutamiseks = open(täht+".txt", "w", encoding="UTF-8")
        if fail_kirjutamiseks:
            print(f"Fail {täht}.txt loodud")
        tähti_kokku = 0
        for rida in f:
            tykeldus = rida.split(" ")
            t = tykeldus[1][0]
            t, täht = t.upper(), täht.upper()
            if täht[0] == t:
                tähti_kokku+=1
                fail_kirjutamiseks.write(str(rida))
                #print(tykeldus[1])
        f.close()
        fail_kirjutamiseks.close()
        if tähti_kokku == 0:
            print(f"Tähega '{täht}' perenimesid ei leitud")
        else:
            print(f"Faili lisatud nimesid kokku:{tähti_kokku} ")
    except:
        print("Mingi jama!") 


def aastaaeg(fail, aastaaeg="kevad"):
    '''Leiab teatud aastaajal võitnud inimesed'''
    aastaajad = {
        'sügis': ['September', 'October', 'November'],
        'talv': ['December', 'January', 'February'],
        'kevad': ['March', 'April', 'May'],
        'suvi': ['June', 'July', 'August']}
    try:
        f = open(fail, encoding="UTF-8")
        fail_kirjutamiseks = open(aastaaeg+".txt", "w", encoding="UTF-8")
        if fail_kirjutamiseks:
            print(f"Fail {aastaaeg}.txt loodud")
        for rida in f:
            tykeldus = rida.split(" ")
            for aeg in aastaajad:
                if tykeldus[4] in aastaajad[aeg]:
                    if aastaaeg==aeg:
                        fail_kirjutamiseks.write(str(rida))
        f.close()
    except:
        print("Mingi jama!")

def linnad(fail, linn="Riga"):
    '''Leiab teatud linnas võitnud inimesed'''
    try:
        f = open(fail, encoding="UTF-8")
        fail_kirjutamiseks = open(linn+".txt", "w", encoding="UTF-8")
        if fail_kirjutamiseks:
            print(f"Fail {linn}.txt loodud")
        for rida in f:
            tykeldus = rida.split(" ")
            if tykeldus[3]==linn:
                fail_kirjutamiseks.write(str(rida))
        f.close()
    except:
        print("Mingi jama!")

def paarisPaaritu(fail):
    '''Leiab paaris või paaritud võidusummad'''
    try:
        f = open(fail, encoding="UTF-8")
        fail_kirjutamiseks = open("paaris.txt", "w", encoding="UTF-8")
        if fail_kirjutamiseks:
            print(f"Fail paaris.txt loodud")
        for rida in f:
            tykeldus = rida.split(" ")
            if int(tykeldus[5])%2==0:
                fail_kirjutamiseks.write(str(rida))
        f.close()
    except:
        print("Mingi jama!")

def sugu(fail, sugu="mees"):
    '''Leiab võitjad soo järgi'''
    try:
        f = open(fail, encoding="UTF-8")
        fail_kirjutamiseks = open(sugu+".txt", "w", encoding="UTF-8")
        if fail_kirjutamiseks:
            print(f"Fail {sugu}.txt loodud")
        for rida in f:
            tykeldus = rida.split(" ")
            if sugu=="mees":
                if int(tykeldus[2][0])%2!=0:
                    fail_kirjutamiseks.write(str(rida))
            else:
                if int(tykeldus[2][0])%2==0:
                    fail_kirjutamiseks.write(str(rida))
        f.close()
    except:
        print("Mingi jama!")

def sarnasedTähed(fail):
    '''Leiab sama nime ja perenime algustähed'''
    try:
        f = open(fail, encoding="UTF-8")
        fail_kirjutamiseks = open("sarnasedTähed.txt", "w", encoding="UTF-8")
        if fail_kirjutamiseks:
            print(f"Fail sarnasedTähed.txt loodud")
        for rida in f:
            tykeldus = rida.split(" ")
            if tykeldus[0][0]==tykeldus[1][0]:
                fail_kirjutamiseks.write(str(rida))
        f.close()
    except:
        print("Mingi jama!")

def main():
    print("#"*30)
    print("Programm leiab infot Andmed lotovõitude kohta")
    print("Vali soovitud tegevus numbriga. Kui soovid programmist väljuda, jäta valik tühjaks")
    print("Valikud salvestatakse tekstifaili")
    print("1 - vali perenime algustähe järgi")
    print("2 - vali aastaaja järgi")
    print("3 - vali linna järgi")
    print("4 - vali paaris või paaritu arvu järgi")
    print("5 - vali soo järgi")
    print("6 - vali sarnaste nime algustähtede järgi")
    print("#"*30)
    loop = 1
    while loop==1:
        try:
            valik = input("Tee valik 1-6: ")
            if valik == "1":
                valik2 = input("Vali täht (A-Z): ")
                algustäht(fail, valik2)
                print("-----------")
            elif valik == "2":
                valik2 = input("Vali aastaaeg (kevad/suvi/sügis/talv): ")
                aastaaeg(fail, valik2)
                print("-----------")
            elif valik == "3":
                valik2 = input("Vali linn: ")
                linnad(fail, valik2)
                print("-----------")
            elif valik == "4":
                paarisPaaritu(fail)
                print("-----------")
            elif valik == "5":
                valik2 = input("Vali sugu (mees/naine): ")
                sugu(fail, valik2)
                print("-----------")
            elif valik == "6":
                sarnasedTähed(fail)
                print("-----------")
            else:
                loop=0
                print("Tänan, et kasutasite meie programmi")
        except:
            print("Mingi jama")
    

if __name__ == "__main__":
    main()



