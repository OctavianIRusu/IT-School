def is_even(number):
    # scop local - ce se intampla in functie ramane in functie
    if number % 2 == 0:
        return True
    else:
        return False
    
# Main

a = 3

a_even = is_even(a)

print(f"Variabila a este numar par? {a_even}")

# End main