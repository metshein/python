def banner(t):
    return t.upper()
    
kordus = int(input("Mitu korda soovid: "))
tekst = input("Lisa tekst: ")

for x in range(kordus):
    print(banner(tekst))

