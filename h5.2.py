ringid = int(input("Ringide arv:  "))
porgandid = 0
for x in range(1,ringid+1):
    if x%2==0:
        porgandid+=x
print(porgandid)