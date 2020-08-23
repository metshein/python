from tkinter import *

#akna seaded
aken = Tk()
aken.title('KABE')

#lõuendi loomine
louend = Canvas(aken, width=360, height=360)
louend.pack()

must = '#000'
valge = '#fff'
counter=0
i = 0
while i <= 320:
    j = 0
    while j <= 320:
        counter+=1
        #kujundite loomine
        louend.create_rectangle(i, j, i+40, j+40, fill=valge)
        print(counter)
        if counter%2==0 and j<120:
            louend.create_oval(i+5, j+5, i+35, j+35, outline="#000", fill="#fff", width=1)
        if counter%2==0 and j>200:
            louend.create_oval(i+5, j+5, i+35, j+35, outline="#fff", fill="#000", width=1)
            
        must,valge = valge, must
        j += 40
    i += 40




aken.mainloop()



    
    