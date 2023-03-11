# Creați un dicționar cu numele și vârsta a trei persoane. Creați o listă
# cu numele acestor persoane și sortați lista în ordine alfabetică inversă.
# Afișați lista sortată.

ages = {"Ion": 23, "Maria": 30, "Andrei": 32}
names = list(ages.keys())
names.sort(reverse=True)

print(names)