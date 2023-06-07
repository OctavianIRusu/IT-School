r_caps = range(65, 91)
k = 0

for i in r_caps:
    k += 1
    print(chr(i), end = " ")

    if k % 6 == 0:
        print()


# ord() - indica codul ASCII pentru un anume simbol

print(ord("G")) # intre literele mari si mici = diferenta de 32

print(chr(ord("A") + 32))