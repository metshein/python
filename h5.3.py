fail = open("konto.txt", encoding="UTF-8")
sisse = []
for rida in fail:
    if float(rida)>0:
        sisse.append(float(rida))
fail.close()

for x in sisse:
    print(x)

