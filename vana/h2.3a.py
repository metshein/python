vanus = int(input("Vanus: "))
sugu = input("Sugu m/n: ")
tyyp = int(input("Vali treeningu tüüp:\n1 - tervis\n2 - põhi\n3 - intensiiv\nVali number: "))
maxPulss = 0
minPulss = 0

if sugu=="m" or sugu=="M":
    pulsisagedus = 220 - vanus
else:
    pulsisagedus = 206-(vanus-vanus*0.12)
    
if tyyp == 1:
    maxPulss = round(pulsisagedus-pulsisagedus*0.5)
    minPulss = round(pulsisagedus-pulsisagedus*0.3)
elif tyyp == 2:
    maxPulss = round(pulsisagedus-pulsisagedus*0.3)
    minPulss = round(pulsisagedus-pulsisagedus*0.2)
else:
    maxPulss = round(pulsisagedus-pulsisagedus*0.2)
    minPulss = round(pulsisagedus-pulsisagedus*0.13)
    
print("Pulsisagedus peaks olema vahemikus",maxPulss,"kuni",minPulss)