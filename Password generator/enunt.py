# Nu de putine ori ai avut nevoie de o parola complexa care sa respecte anumite
# criterii. Te-ai gandit sa folosesti un generator on-line dar stii ca poate
# nu este cea mai sigura metoda. Asa ca hai sa construim unul in care sa ai incredere.

# programul trebuie sa afiseze in consola o parola generata in functie de configuratia
# aleasa de utilizator
# configuratia este specificata prin raspunsul utilizatorului la intrebarile:
    # password length [number]:
    # use digits [y/n]?
    # use symbols [y/n]?

# parola generata nu trebuie sa contina caractere consecutive identice (ex: aa3de33)

# citirea informatiilor de la tastatura se face in functii diferite pentru fiecare intrebare:
    # get_user_length -> returneaza (int) ce a raspuns utilizatorul la intrebare
    # get_user_use_digits -> returneaza (bool) True daca userul introduce y, False daca altceva
    # get_user_use_symbols -> idem