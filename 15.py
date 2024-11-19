# Metshein 19.11.24
# Ülesanne 15


import turtle
import random

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# kiirused
ristkyliku_kiirus = 20
kiirus = 10

# skoori lugemine
skoor = 0

# ristküliku funktsioonid
def liigu_vasakule():
  x = ristkylik.xcor()
  if x > -280:
    ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
  x = ristkylik.xcor()
  if x < 280:
    ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
  nurk = ring.heading()
  if ring.xcor() >= 300 or ring.xcor() <= -300:
    uus_nurk = 180 - nurk
    if uus_nurk < 0:
      uus_nurk += 360
    ring.setheading(uus_nurk)
  if ring.ycor() >= 300 or ring.ycor() <= -300:
    uus_nurk = 360 - nurk
    ring.setheading(uus_nurk)

def tuvasta_kokkuporge():
    #if ring.ycor() <= -240 and ((ring.xcor() > ristkylik.xcor()-10) or (ring.xcor() > ristkylik.xcor()+10)):
    if ring.ycor() <= -240 and ((ring.xcor() > ristkylik.xcor()-50) and (ring.xcor() < ristkylik.xcor()+50)):
        nurk = ring.heading()
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)
        global skoor
        skoor += 1
        print(f"Skoor: {skoor}")

def ring_liigu():
  ring.forward(kiirus)
  peegelda_porkumisel()
  tuvasta_kokkuporge()
  aken.update()
  aken.ontimer(ring_liigu, 20)


# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()

aken.mainloop()
