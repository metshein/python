# 18.10.24 Metshein
# Ülesanded 6
import turtle
import math

# Redel
## Matem
korgus = 4.4
nurk = 53

kaugus = abs(korgus / math.tan(nurk))
c = math.sqrt((korgus**2) + (kaugus**2))
print(kaugus, c)
#Joonis
kordaja = 20
turtle.fd(kaugus*kordaja)
turtle.left(90)
turtle.fd(korgus*kordaja)
turtle.left(180-67)
turtle.fd(c*kordaja)







turtle.done()