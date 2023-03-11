# Creati un program care sa afiseze:
    
#     $
#    ***
#   *****
#  *******
# *********

print("{:^9}".format("$"))
for i in range(3, 10, 2):
    v = "*" * i
    print(f"{v:^9}")