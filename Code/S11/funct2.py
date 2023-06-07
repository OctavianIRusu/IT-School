def add_one(number):
    # scop local
    number +=1

# Main - scop global

a = 3

print(f"a={a}")
add_one(a)
print(f"a={a}")
