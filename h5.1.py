fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
for rida in fail:
    vastuvõetud.append(int(rida))

aasta = int(input("Vali aasta 2011-2019: "))
valik = vastuvõetud[aastad.index(aasta)]
print(aasta, "oli vastuvõetuid", valik)
fail.close()

print(aastad)
print(vastuvõetud)