# 19.12.24
# Metshein
# Ülesanne 07


nimi = ["Jyri Pootsman","Mari Jyrgens", "ans Maali", "Terminaator - Juulikuus lumi on maas"]

# for i in nimi:
#     print(i)
    
for i in range(4):
    print(f"{i+1}. {nimi[i]}")
    
valik = int(input("Vali lugu (1-4): "))
print(f"Mängin: {nimi[valik-1]}")
    
    
    