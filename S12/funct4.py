# def zero_one(lst):
#     lst[0] = 1


# Indicat de creat o noua functie, nu de modificat cea existenta
def zero_one(lst):
    lst_in = lst[:]
    lst_in[0] = 1
    return lst_in

matrix = [
    [0, 3, 4, 4],
    [2, 34, 24, 43]
]

print(matrix)
m = zero_one(matrix)    # pass by reference
print(matrix)
print(m)