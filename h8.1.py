def juurdekasv(s,j):
    jk = float(s)*0.4047*float(j)
    return round(jk,2)

f = input("Fail: ")
j= float(input("Juurdekasv: "))
piir = float(input("Piir: "))
count = 0
#f="andmed.txt"
fail = open(f, encoding="UTF-8")
for rida in fail:
    if float(rida)>piir:

        print(juurdekasv(float(rida),j))
        count+=1
    else:
        print("Metsatükki ei võeta arvesse")
print("Arvutitati "+str(count)+" metsatüki juurdekasv.")
fail.close()


