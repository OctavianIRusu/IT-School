# D:\Curs Programare Python\IT School 2023\S22\atm_project # absolute path
# S22\atm_project # relative path

from pathlib import Path
from datetime import datetime

# . directorul curent, .. directorul de mai sus

working_dir = Path('.')  # current working directory

print(working_dir)
print(type(working_dir))

print(working_dir.absolute())

script_path = Path(__file__)  # calea catre fisierul in care operez
print(f"Script path: {script_path}")
print(f"Script parent directory {script_path.parent.parent}")

print(f"{script_path} exists? {script_path.exists()}")
start_time_path = script_path.parent / "program_data" / "start_time"
print(start_time_path)

# # create a folder
# if not start_time_path.parent.exists():
#     start_time_path.parent.mkdir()
#     # mkdir = make directory
#     print(f"Created {start_time_path.parent}")

start_time_path.mkdir(exist_ok=True, parents=True)

print(start_time_path.is_dir())
print(start_time_path.is_file())

# w = scriere text
# r = citire text
# a = adaugare text
# wb = scriere binara
# rb = citire binara
# ab = adaugare binara

# fis1 = open(start_time_path / "test.txt", "w")  # path absolut
# fis1.close()

now = datetime.now()
now_file_name = now.strftime("%Y%m%d_%H%M%S.txt")

# context manager - va inchide automat fisierul
with open(start_time_path / now_file_name, "w") as fout:  # fout => file descriptor (FD)
    fout.write("NO ERRORS!")

print("File operation done!")
