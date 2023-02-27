user_ids = [324, 345, 536, 64, 78]

print(user_ids[2])
print("Lungime lista: ", len(user_ids))
print(user_ids[len(user_ids)-1])
print("Ultimul element: ", user_ids[-1])
print("Primul element: ", user_ids[0])

index_dorit = 4

if len(user_ids) > index_dorit:
    print("Elementul de pe pozitia", index_dorit, "este", user_ids[index_dorit])
else:
    print("Indexul", index_dorit, "nu exista!")
print("END")