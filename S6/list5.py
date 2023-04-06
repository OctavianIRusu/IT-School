temp = [33, 22, 34, 21, 22, 0]
to_remove = 22

print(temp)

print(to_remove, "apare de", temp.count(to_remove), "ori")

if 22 in temp:
    print("A fost cald")
    if temp.count(22) > 1:
        print("A fost foarte cald")

temp1 = temp.copy()
temp1.reverse()
print(temp1)
print(temp)

print("Temperatura maxima", max(temp))
print("Temperatura minima", min(temp))