def tervitus(x):
    print("Võõrustaja: \"Tere!\"")
    print("täna "+str(x)+". kord tervitada, mõtiskleb võõrustaja.")
    print("Külaline: \"Tere, suur tänu kutse eest!\"")
x = int(input("Sisestage külaliste arv: "))
for i in range(1,x+1):
    tervitus(i)