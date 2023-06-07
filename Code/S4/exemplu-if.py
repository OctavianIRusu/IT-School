print("MENU")
print("Alege o optiune:")
print("1. Adauga carte citita")
print("2. Sterge o carte")

choice = int(input ("Introduceti un numar si apoi ENTER: "))

if choice == 1:
    print("Introdu detaliile cartii")
elif choice == 2:
    print("Alege o carte pe care sa o stergi")
else:
    print("Optiunea aleasa nu exista")

print("END")