# Modificare dictionar - sau adaugare cheie noua

dict1 = {
    "key1": 1,
    "key2": {
        "key1": 1,
        "key2": ["elem1", "elem2"]
    }
}

dict1["key1"] = 2

dict1["key3"] = set()

del dict1["key2"]

print(dict1)