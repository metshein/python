# 3. Ülesanne
# Metshein 05.12.24
import turtle
#3.1
nimi = "Imre" #sõne, string, str
vanus = 20 #int, integer, täisarv
keskmine_hinne = 6.5 #komarv, float
#plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))
#komaga saan mitu asja printida
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne)
#lause vormindamine lünkadega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}")

#3.7kolmnurk
kylje_pikkus = 100
nurk = 120
varv = "red"

turtle.speed(0)
turtle.color(varv)
#kolmnurk
turtle.forward(kylje_pikkus)
turtle.left(nurk) 
turtle.forward(kylje_pikkus) 
turtle.left(nurk) 
turtle.forward(kylje_pikkus) 
turtle.left(nurk)

turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

#kolmnurk 2
turtle.fd(kylje_pikkus)
turtle.lt(nurk) 
turtle.fd(kylje_pikkus) 
turtle.lt(nurk) 
turtle.fd(kylje_pikkus) 
turtle.lt(nurk)

turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

#kolmnurk 3
turtle.forward(kylje_pikkus)
turtle.left(nurk) 
turtle.forward(kylje_pikkus) 
turtle.left(nurk) 
turtle.forward(kylje_pikkus) 
turtle.left(nurk)



turtle.done()




