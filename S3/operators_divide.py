a = 234
b = 26

print(a/b)
print("Catul impartirii: " + str(a//b))
print("Restul impartirii: " + str(a%b))     #procent sau modulo

#modulo poate fi folosit pentru a testa daca un numar este par sau impar

test_number = 234
rest = test_number % 2
is_even = not bool(rest)    #not face negatie

print(str(test_number) + " este par", is_even)