# citeste de la tast numele cu input
# creare fisier in acelasi folder cu script-ul - fisier1.txt cu numele de citit

from pathlib import Path

nume = input("Introdu numele: ")

this_folder_path = Path(__file__).parent
file_name = "fisier1.txt"

with open(this_folder_path / file_name, "w") as fout:
    fout.write(nume)

print(f"The txt file named {file_name} was created!")
