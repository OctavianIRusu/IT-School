# Print a justified string histogram for lorem variable.
#     EX:
#     l ................ 10
#     i ................ 20
#     j .................33

lorem = "Lorem Ipsum is simply dummy lorem of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy lorem ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

chars = lorem.lower().replace(",","").replace(".","").replace("\'","").replace(" ","")

histogram = []

for i in chars:
    if i not in histogram:
        histogram.append(i)
    else:
        continue

for v in histogram:
    print("{:.<10}{: >}".format(v, chars.count(v)))