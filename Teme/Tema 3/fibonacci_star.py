n = int(input("Introduceti numarul de linii: "))

fibonacci = [1, 1]

while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

for i in fibonacci:
    print(i * "*")
