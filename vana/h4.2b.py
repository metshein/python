from tkinter import *
aken = Tk()
aken.title('Tkinter "Liiklusmärk"')
tekst = Label(aken, text="Liiklusmärk", font="Tahoma 16 bold").pack()
louend = Canvas(aken, width=500, height=500, bg="#fff")
louend.pack()
louend.create_oval(50, 50, 450, 450, outline="#f11", fill="#fff", width=30)
louend.create_text(250,250,font="Arial 200 bold", text="70")
aken.mainloop()
