import pickle
from pathlib import Path

from lib.complaint import Complaint
from lib.interface import CLIMenu

ROOT = Path(__file__).parent

menu = CLIMenu("Complaint booklet", {
    "Adauga plangere": lambda: print("Adauga plangere"),
    "Rezolva plangere": lambda: print("Rezolva plangere"),
    "Vezi plangeri nerezolvate": lambda: print("Vezi plangeri nerezolvate"),
})

# menu.show_main()

# c1 = Complaint("Am o problema", "Random text asfboasjfknkasaf")
# c2 = Complaint("Am o problema1", "Random text asfboasjfknkasaf")
# c3 = Complaint("Am o problema2", "Random text asfboasjfknkasaf")
# c4 = Complaint("Am o problema3", "Random text asfboasjfknkasaf")
# c5 = Complaint("Am o problema4", "Random text asfboasjfknkasaf")

# l1 = [c1, c2, c3, c4, c5]

# for i in l1:
#     print(i.id, i.title)

# try:
#     with open(ROOT / "complaints.dump", "wb") as fout:
#         pickle.dump(l1, fout)
# except OSError as err:
#     print(err)

dump_file = ROOT / "complaints.dump"

try:
    with open(dump_file, "rb") as fin:
        unknown = pickle.load(fin)
except OSError as err:
    print(err)
else:
    for i in unknown:
        print(i.id, i.title)
