# 18.10.24 Metshein
# Ülesanded 5
import random
import turtle

#4. Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
# 1 kull
# 0 kiri
suv = random.randint(0,1)
kasutaja_valik = input("Kull või kiri: ")
if (suv==1 and kasutaja_valik=="kull") or (suv==0 and kasutaja_valik=="kiri"):
    varv = "green"
else:
    varv = "red"
    
print(suv)
turtle.color(varv)
turtle.circle(50, 360)
turtle.done()



'''
#3. Matemaatika test (randint)
a, b = random.randint(1,10), random.randint(1,10)
vastus = int(input(f"Lisa vastus {a}*{b}="))
if vastus == a*b:
    print("Tubli")
else:
    print("Loll oled!")

#2. Ilmaennustuse rakendus (and)
c = 15
if c < 0:
    print("Talveriided")
elif c >= 0 and c <=15:
    print("Kevad-sügis")
else:
    print("Suvi")



#1. Vanusepiiranguga üritus
vanus = 18
if vanus >= 18:
    print("Saab sisse.")
else:
    print("Liiga noor!")

'''