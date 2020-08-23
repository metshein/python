from random import randint
tyybid = int(input("Mitu poissi tahab õunu 0-7? "))
ounad = 14
for x in range(tyybid):
    suv = randint(1,2)
    ounad-=suv
    print(suv)
print("Lumivalgekesele jäi:",ounad)
