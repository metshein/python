def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))
    
f = "sunnikuupaevad.txt"
#f = input("Lisa fail ")
fail = open(f, encoding="UTF-8")

kuup = []
for rida in fail:
    kuup.append(rida.rstrip())
    #r = elutee(rida.rstrip())
    #eluteenumbrid.append(r)
fail.close()

print(kuup)

for k in range(len(kuup)):
    r = elutee(kuup[k])
    for i in range(1,10):
        uusFail = open("eluteenumber"+str(i)+".txt", 'a+',encoding="UTF-8")
        if r==i:
            uusFail.write(kuup[k]+"\n")
            print(kuup[k])
        fail.close()

    
