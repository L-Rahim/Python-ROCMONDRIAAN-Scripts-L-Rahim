print("Hello, World!")

tekst = "Hallo"
getal = 5
kommagetal = 3.14

print(tekst)
print(getal)
print(kommagetal)

naam = input("Wat is je naam? ")
leeftijd = input("Hoe oud ben je? ")

print(f"Hallo, {naam}! Je bent {leeftijd} jaar oud.")

getal1 = 8
getal2 = 4

print(getal1 + getal2) 
print(getal1 - getal2)
print(getal1 * getal2)
print(getal1 / getal2)

boeken = ["De hobbit", "1984", "To Kill a Mockingbord"]

print(boeken)

boeken.append("Pride and Prejudice")
print(boeken)

leeftijd = int(input("Hoe oud ben je? "))

if leeftijd >= 18:
    print("Je bent oud genoeg on te stemmen.")
else:
    print("Je bent niet oud genoeg om te stemmen.")

for i in range(1, 11):
    print(i)

def hallo():
    print("Hallo, wereld!")

hallo()

