# Group product codes from product_code_list in a dictionary by last char.

product_code_list = [
    "mmf2",
    "xdfr",
    "ef3r",
    "efc2",
    "sddf"
    "weee"
]

dict = {}

for i in product_code_list:
    if i[-1:] not in dict:
        dict[i[-1:]] = [i]
    else:    
        dict[i[-1:]].append(i)

print(dict)