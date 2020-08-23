import random
istekoht = ""
otsus = ""
valiIstekoht = input("Istekoht ise/loos: ")
if valiIstekoht == "ise":
    otsus = "Valisite ise. "
    valik = input("Aknaääres (aken/muu): ")
    if valik == "aken":
        istekoht = "Aknakoht"
    else:
        istekoht = "Vahekäigukoht"
else:
    otsus = "Istekoht loositi. "
    loos = random.randint(1,3)
    if loos == 1:
        istekoht = "Aknakoht"
    else:
        istekoht = "Vahekäigukoht"
print(otsus+istekoht)