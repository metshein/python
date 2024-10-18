import math

# Andmed
korgus = 4.4  # meetrit
nurk = math.radians(53)  # teisendame kraadid radiaanideks

# Kauguse arvutamine tangensfunktsiooni abil
kaugus = korgus / math.tan(nurk)

# Redeli pikkuse arvutamine Pythagorase teoreemi abil
pikkus = math.sqrt(korgus**2 + kaugus**2)

# Ümardame vastused kahe komakohani
kaugus_2_komakohta = round(kaugus, 2)
pikkus_2_komakohta = round(pikkus, 2)

print(kaugus_2_komakohta, pikkus_2_komakohta)