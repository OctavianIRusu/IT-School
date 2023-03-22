import argparse

print("Hello!")

argparser = argparse.ArgumentParser()
argparser.add_argument("symbol", type=str)
argparser.add_argument("mul", type=int)
args = argparser.parse_args()

print(args.symbol * int(args.mul))

print("Bye!")

# de adaugat un argument (separator)
# de adaugat un argument optional -v (verbose) = afiseaza mesajele hello si bye daca este setat la true