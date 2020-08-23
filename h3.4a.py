ringid = int(input("Ringide arv: "))
loop = 0
porgandid = 0
while loop<ringid:
    loop+=1
    uus = int(loop*(loop+1)/2)
    porgandid += uus
print("Porgandite koguarv on "+str(porgandid)+".")