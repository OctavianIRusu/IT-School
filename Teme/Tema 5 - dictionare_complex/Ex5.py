# Creați o listă cu cinci dicționare, fiecare dicționar conținând numele și
# notele unui elev. Iterați prin lista și calculați media notelor fiecărui
# elev. Adăugați media ca o intrare suplimentară în fiecare dicționar.
# Sortați lista în funcție de medie și afișați numele și nota fiecărui elev
# în ordine crescătoare a mediilor.

elevi = [
    {"nume": "Elena", "note": [4, 5, 6]},
    {"nume": "Sandra", "note": [8, 7, 6]},
    {"nume": "Cosmin", "note": [10, 5, 6]},
    {"nume": "Florin", "note": [5, 5, 8]},
    {"nume": "Laura", "note": [8, 9, 9]}
]   

for elev in elevi:
    elev["media"] = sum(elev["note"]) / len(elev["note"])

sorted_list = sorted(elevi, key=lambda x: x["media"])

for elev in sorted_list:
    print(f"{elev['nume']}: {elev['note']}, media: {elev['media']}")

