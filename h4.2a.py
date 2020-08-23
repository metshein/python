from tkinter import *
aken = Tk()
aken.title('Tkinter "Haapsalu lipp"')
tekst = Label(aken, text="Haapsalu lipp", font="Tahoma 16 bold").pack()
louend = Canvas(aken, width=500, height=300)
louend.pack()

sinine = '#0f47af'
valge = '#fff'
x = 20
x2 = x+80

for i in range(3):
    louend.create_rectangle(50, x, 200, x2, fill=sinine, width=0)
    louend.create_rectangle(200, x, 450, x2, fill=valge, width=0)
    x=x+80
    x2=x+80
    sinine, valge = valge, sinine

aken.mainloop()