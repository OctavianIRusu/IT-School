matrix = [
    ["Ionel", [4, 5, 6, 7, 8]],
    ["Ionut", [4, 7, 7, 8, 9]],
    ["Andrei", [7, 7, 8, 9, 10]],
    ["Sandu", [4, 5, 5, 3, 5]],
]

print(matrix[0][1][0])
print(sorted(matrix))

for i in matrix:
    print(i[0], "cea mai mare nota", max(i[1]))

for i in matrix:
    print(i[0], "media", sum(i[1])/len(i[1]))

    # numele elevului cu media cea mai mare, media cea mai mica, si cu media sub 5