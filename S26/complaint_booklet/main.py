from lib.interface import ListUnsolved, MenuUserChoice, AddItem, ExitItem, SolveOne
from lib.complaint import Complaint, Booklet
from pathlib import Path
import pickle

ROOT = Path(__file__).parent
b1 = Booklet()

main_menu = MenuUserChoice("Caiet de reclamarii")
main_menu.add_choice(ListUnsolved("Vezi reclamatii nerezolvate", b1))
main_menu.add_choice(AddItem("Adauga reclamatie", b1))
main_menu.add_choice(SolveOne("Rezolva reclamatie", b1))
main_menu.add_choice(ExitItem("Iesire"))

while True:
    main_menu.execute()

# menu.show_main()

# for i in l1:
#     print(i.id, i.title)

# try:
#     with open(ROOT / "complaints.dump", "wb") as fout:
#         pickle.dump(l1, fout)
# except OSError as err:
#     print(err)

# dump_file = ROOT / "complaints.dump"

# try:
#     with open(dump_file, "rb") as fin:
#         unknown  = pickle.load(fin)
# except OSError as err:
#     print(err)
# else:
#     for i in unknown:
#         print(i.id, i.title)
