valik = input(" jukebox.txt\n 80ndad.txt\n eesti_muusika.txt\n edm.txt\nVali fail: ")

fail = open(valik, encoding="UTF-8")
laulud = []
count = 1
for rida in fail:
    laulud.append(rida)
    nimekiri = str(count)+"."+rida
    print(nimekiri,end="")
    count+=1
fail.close()

valik2 = int(input("\n\nVali laul nr: "))
print(laulud[valik2-1])