# Creeaza o lista de cumparaturi cu cateva elemente in ea. (lista de stringuri).
# Creeaza un string formatat pentru a afisa ceva asemanator cu : Azi trebuie sa cumperi: mere, pere, struguri.

cumparaturi = ["mere", "pere", "banane", "kiwi"]
print("Astazi trebuie sa cumpar urmatoarele fructe: {}.".format(", ".join(cumparaturi)))