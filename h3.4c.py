arv = int(input("Sisestage täisarv: "))
terad = 1
q = 2
start = 1
while start<=arv:
    v=terad*q**(start-1)
    summa=v
    start+=1
print("Nisuteri", arv,"Ruudu eest:",summa)


"""
a = 1
q = 2
teri = 24
for x in range(1,teri+1):
    v=a*q**(x-1)
    summa=v
print("Nisuteri", teri,"Ruudu eest:",summa)
"""
    