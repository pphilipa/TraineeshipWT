#csv bestand van: https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6

import pandas 

print('Start csv read applications')

df=pandas.read_csv('pokemon.csv')
print(df["Name"])

for r,rij in df.iterrows():
    print(r)
    print("De huidige naam is: " + rij["Name"])
    