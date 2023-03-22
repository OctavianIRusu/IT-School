def product(a, b):
    """Calculate the product of a and b."""
    return a * b

# Apelarea functiei cu un numar nedefinit de argumente (oricate dorim)
def n_product(*args):
    p = 1
    for i in args:
        p *= i
    return p

print(n_product(1))
print(n_product(1, 2))
print(n_product(1, 2, 3))

# Apelarea functiei cu minim 2 argumente:

def new_function(a, b, *args):
    p = a * b
    for i in args:
        p *= i
    return p