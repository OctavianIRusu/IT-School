# Scopul local are acces la valoarea din scopul global
# In schimb, din global nu putem avea acces in scopul local
# Globale - constantele care nu se modifica in cod


PI = 3.14

def hello():
    b = PI + 10
    print(f"b din functia hello are valoarea: {b}")

hello()
print(PI)
# print(b) - o sa dea eroare, nu avem acces la aceasta valoare