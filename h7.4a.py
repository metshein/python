f = input("Lisa fail ")
fail = open(f, encoding="UTF-8")
kokku = 0
kindlalt = 0
for rida in fail:
    kokku+=1
    rida = rida.split()
    if rida[0]=="+":
        kindlalt+=1
fail.close()

def eelarve(x):
    toit = 10
    ruum = 55
    arve = x * 10 + 55
    return arve

print("")
print("Kutsutud:",kokku,"inimest")
print(kindlalt,"inimest tuleb")
print(eelarve(kokku),"eur")
print(eelarve(kindlalt),"eur")


