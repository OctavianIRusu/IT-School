n = 0

while n <= 100:
    if n > 1:
        i = 2
        while n > i:
            if n % i == 0:
                break
            i += 1
        else:
            print(n)
    n += 1
