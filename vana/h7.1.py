f = input("F: ")
fail = open(f, encoding="UTF-8")
for rida in fail:
    s = rida.upper()
    for r in (("Ä", "AE"), ("Õ", "OE"), ("Ö", "OE"), ("Ü", "UE")):
        s = s.replace(*r)
    print(s,end="")
fail.close()

