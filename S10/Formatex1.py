auto = {
    "marca": "Audi",
    "model": "A4",
    "usi": 4
}

TEMPLATE_AUTO = "Detin o masina marca {}, model {} si are {} usi."

print(TEMPLATE_AUTO.format(auto["marca"], auto["model"], auto["usi"]))