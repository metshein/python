def kuu_nimi(kuu):
    kuud = ['','jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    return kuud[kuu]

def kuupäev_sõnena(kp):
    kuud = ['','jaanuar','veebruar','märts','aprill','mai','juuni','juuli','august','september','oktoober','november','detsember']
    dd,mm,yyyy = kp.split(".")
    kuup = dd+". "+kuu_nimi(int(mm))+" "+yyyy+". a"
    return kuup

lisakp = input("lisa kp: ")

print(kuu_nimi(1))
print(kuupäev_sõnena(lisakp))