from datetime import datetime
kuupäev_kellaeg = datetime.today()


f = input("tekst: ")
fail = open("paevik.txt", "a+", encoding="UTF-8")
fail.write("\nKuupäev ja kellaeg: " + str(kuupäev_kellaeg))
fail.write("\n"+f+"\n")
fail.close()