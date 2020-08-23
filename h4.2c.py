from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')

#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine
louend.create_rectangle(100, 200, 400, 400, fill='#99CC33')
louend.create_rectangle(150, 250, 250, 400, fill='#66BB22')
louend.create_polygon(100, 200, 400, 200, 250, 50)

aken.mainloop()