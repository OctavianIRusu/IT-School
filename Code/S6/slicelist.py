temperaturi = [91, 61, 80, 5, -44, -39, -87, 52, -68, -7, -25, -82, 1, 60, -45, -83, 9, 81, 54, -30, 49, -39, -65, -57, 18, 57, -70, -100, -53, 36, -69, 93, -82, 89, 90, -89, 70, 64, -18, -99, 68, -49, 13, -96, -5, 83, 98, 57, 26, -27, 31, 54, 45, 7, -62, 56, 66, 82, -79, 50, -54, -79, -75, 30, 43, 81, 23, -44, -15, 3, 9, -67, -80, 77, 10, -22, -18, -47, 57, 21, -98, -37, 83, -62, 25, 65, -69, 15, -75, -9, 66, -79, 15, -32, -54, 32, -3, -89, -33, 28]

print(len(temperaturi))

# sa se afiseze primele 10

# Method 1
new_temp = []

for i in range(10):
    new_temp.append(temperaturi[i])

# Method 2
new_temp2 = temperaturi[0:10]   # sau temperaturi[:10] - temperaturi[:] creeaza o copie a listei
print(len(new_temp2))