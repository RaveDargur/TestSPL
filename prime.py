# Primzahlen Ueberpruefen

zahl = input("Geben Sie eine Zahl ein")
z = int(zahl)
cor = True

for i in range(2,z):
    if (z % i == 0) :
        cor = False

if(cor == True):
	print("Primzahl")
else:
	print("keine Primzahl")
