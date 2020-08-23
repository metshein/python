def parandatud_tulemus(m,cm):
    #tegelikTulemus = viganeTulemus + mõõteparandus / 100
    jk = m+cm/100
    return round(jk,2)

#f = input("Fail: ")
p= float(input("Parandus: "))
n = float(input("Normatiiv: "))
f="kaugus.txt"
norm = []
fail = open(f, encoding="UTF-8")
for rida in fail:
    print(parandatud_tulemus(float(rida),p))
    if float(rida)>n:
        norm.append(parandatud_tulemus(float(rida),p))
print("Normi ületanud",len(norm))
print("Normi ületanud keskmine",sum(norm)/len(norm))
fail.close()
