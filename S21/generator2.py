import time


def rand_numb():
    a = 0
    b = 1

    while True:
        yield b
        a, b = b, a + b


def pow_of_two():
    a = 0
    while True:
        yield 2 ** a
        a += 1


numb_gen = pow_of_two()

for i in numb_gen:
    time.sleep(1)
    print(i)
