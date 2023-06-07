from pathlib import Path

ROOT = Path(__file__).parent

input_file_path = ROOT / "git.txt"

try:
    with open(input_file_path, "r") as fin:
        content = fin.readlines()
except OSError as err:
    print(err)
else:
    for i in content:
        if i.startswith("#"):
            print(i.strip("\n\r\t "))
