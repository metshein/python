for x in range(0, 3):
    suurus = float(input("Kirja suurus MB: "))
    pk = input("Pealkiri: ")
    manus = input("Manus jah/ei: ")
    if not pk or (suurus>1.0 and manus=="jah"):
        print("Kiri on spämm")
    else:
        print("Kiri ei ole spämm")