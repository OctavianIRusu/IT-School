# Se da lista de mai jos: 
# avand in vedere ca o victorie valoreaza 3 pct. si un egal 1 pct. 

# a) sa se adauge o cheie noua in fiecare dictionar, numele cheii este 'puncte' 
# iar ca valoare va avea numarul de puncte acumulate
# b) sa se afiseze numele echipei campioane
# c) sa se afiseze numele echipei cu cele mai multe egaluri
# d) sa se afiseze podiumul (nume si numar de pct)


rezultate_campionat = [
    {"echipa": "CFR Cluj", "meciuri_jucate": 36, "victorii": 22, "egaluri": 9, "infrangeri": 5},
    {"echipa": "FCSB", "meciuri_jucate": 36, "victorii": 21, "egaluri": 7, "infrangeri": 8},
    {"echipa": "Universitatea Craiova", "meciuri_jucate": 36, "victorii": 18, "egaluri": 11, "infrangeri": 7},
    {"echipa": "Sepsi Sfântu Gheorghe", "meciuri_jucate": 36, "victorii": 15, "egaluri": 11, "infrangeri": 10},
    {"echipa": "Astra Giurgiu", "meciuri_jucate": 36, "victorii": 14, "egaluri": 11, "infrangeri": 11},
    {"echipa": "CS Mioveni", "meciuri_jucate": 36, "victorii": 13, "egaluri": 12, "infrangeri": 11},
    {"echipa": "FC Argeș Pitești", "meciuri_jucate": 36, "victorii": 13, "egaluri": 9, "infrangeri": 14},
    {"echipa": "FC Botoșani", "meciuri_jucate": 36, "victorii": 12, "egaluri": 10, "infrangeri": 14},
    {"echipa": "Gaz Metan Mediaș", "meciuri_jucate": 36, "victorii": 11, "egaluri": 12, "infrangeri": 13},
    {"echipa": "FC Voluntari", "meciuri_jucate": 36, "victorii": 12, "egaluri": 8, "infrangeri": 16},
    {"echipa": "Academica Clinceni", "meciuri_jucate": 36, "victorii": 10, "egaluri": 12, "infrangeri": 14},
    {"echipa": "FC Hermannstadt", "meciuri_jucate": 36, "victorii": 10, "egaluri": 11, "infrangeri": 15}
]
# definire constante
VICTORIE = 3
EGAL = 1

# adaugare cheie noua "puncte" si valorile aferente calculate
for dict in rezultate_campionat:
    dict["puncte"] = dict["victorii"] * VICTORIE + dict["egaluri"] * EGAL

# sa se afiseze numele campioanei

# pct_campioana = 0

# for dict in rezultate_campionat:
#     if dict["puncte"] > pct_campioana:
#         pct_campioana = dict["puncte"]
#         echipa_campioana = dict["echipa"]
#     else:
#         campioana = 0
# print(f"Echipa campioana este {echipa_campioana}, cu {pct_campioana} puncte acumulate.")

rezultate_campionat.sort(key=lambda x: x["puncte"], reverse=True)
print(rezultate_campionat[0]["echipa"])

# sa se afiseze echipa cu cele mai multe egaluri

rezultate_campionat.sort(key=lambda x: x["egaluri"], reverse=True)
print(rezultate_campionat[0]["echipa"])

# sa se afiseze podiumul

rezultate_campionat.sort(key=lambda x: x["puncte"], reverse=True)
podium = rezultate_campionat[:3]

for i in podium:
    print(i["echipa"], i["puncte"])