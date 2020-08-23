def pronksikarva_summa(r):
    #return sum(r)
    kokku = 0
    for i in range(len(r)):
        if r[i] == 1 or r[i] == 2 or r[i] == 5:
            kokku += r[i]
    return kokku

valik = input("Vali fail (mündid.txt): ")
fail = open(valik, encoding="UTF-8")
mündid = []
for rida in fail:
    mündid.append(int(rida))
fail.close()

print(pronksikarva_summa(mündid))
