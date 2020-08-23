ringid = int(input("Ringide arv: "))
loop = 0
porgandid = 0
while loop<ringid:
    loop+=1
    if loop%2==0:
        porgandid+=loop 
print("Porgandite koguarv on "+str(porgandid)+".")
    
    