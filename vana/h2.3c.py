inim = int(input("inimesed: "))
kohti = int(input("kohti: "))
if inim%kohti==0:
    buss = inim//kohti
    yle = kohti
else:
    buss = inim//kohti+1
    yle = inim%kohti

print("Busse vaja:",buss)
print("Viimases bussis inimesi:",yle)

