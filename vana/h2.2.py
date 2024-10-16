punktid = float(input("Punktisumma: "))
if punktid>=0 and punktid<66:
    print("Vähem kui kandideerimiseks vajalik")
elif punktid>=66 and punktid<85:
    print("Kandideerimine vastuvõtule")
elif punktid>=85 and punktid<=100:
    print("Vastuvõtt tagatud")
elif punktid<=0 or punktid>100:
    print("Vigane punktisumma")