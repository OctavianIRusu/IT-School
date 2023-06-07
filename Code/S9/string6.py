user_code = "44563-orusu-0001"

prev = 0

while prev != -1:
    prev = user_code.find("-", prev + 1)
    print(prev)
