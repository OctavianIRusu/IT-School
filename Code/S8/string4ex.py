product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf"
    "weee"
]

# Metoda 1
for i in range(len(product_code_list)):
    product_code_list[i] = product_code_list[i][:-1]+"x"

# Metoda 2
for i, v in enumerate(product_code_list):
    product_code_list[i] = v[:-1] + "x"

print(product_code_list)
