countries = ("Romania", "Albania", "Ungaria")

# method 1
for i in enumerate(countries):
    print(i[0], i[1])

# method 2
for i, j  in enumerate(countries):
    print(i, j)