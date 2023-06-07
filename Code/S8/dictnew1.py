# Sa se extraga elem2 din dictionar

dict1 = {
    "key1": 1,
    "key2": {
        "key1": 1,
        "key2": ["elem1", "elem2"]
    }
}

dict3 = dict1["key2"]["key2"][1]
print(dict3)