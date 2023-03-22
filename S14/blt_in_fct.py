# all - true daca toate valorile din lista evalueaza True
print(all([True, 0]))

# any - true daca oricare element din lista este True
print(any([True, True, False]))

# map - executes a specified function for each item in an iterable
init_lst = [4, 56, 7, 5, 45]
new_lst = map(lambda x: x ** 2, init_lst)
new_list1 = [x ** 2 for x in init_lst]

print(type(new_lst))
print(type(new_list1))

# enumerate - perechi index-valoare dintr-o lista
print(enumerate(init_lst))
for i in enumerate(new_lst):
    print(f"Index: {i[0]} ... valoare: {i[1]}")

# divmod - returneaza catul si restul unei impartiri
cat, rest = divmod(10, 3)
print(f"Catul = {cat} si restul = {rest}")

# zip
names = ["Alex", "Elena", "Victor"]
ids = ["233231", "353533", "253214"]

zp = zip(names, ids)

# for i in zp:
#     print(i)

print(dict(zp))