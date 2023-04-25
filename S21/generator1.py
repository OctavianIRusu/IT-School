def get_numbers():
    return [2, 3, 4, 5, 6, 7, 8, 44, 45, 35, 435]


def get_next_num():
    return 2


print(get_numbers())
print(get_next_num())


# se inlocuieste cuvantul cheie return cu "yield"
# functia rand_numb() este un fel de fabrica de generatoare - defineste cum arata generatorul
# apelarea functiei creeaza generatorul
# in cazul generatorului nu stim cate elemente o sa genereze up front - se calculeaza instant
def rand_numb():
    yield 2


numb_gen = rand_numb()
print(numb_gen)

# try:
#     # functia next apelata pe un generator ne ofera urmatoarea valoare disponibila din generator
#     print(next(numb_gen))
#     # functia next poate ridica eroare daca ramane generatorul fara valori (apelare pana la o limita)
#     print(next(numb_gen))
# except StopIteration:
#     print("End of generator")

for i in numb_gen:
    print(i)
