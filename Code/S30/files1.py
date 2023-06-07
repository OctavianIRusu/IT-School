import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
PHOTO_PATH = ROOT / "poze_nunta"

# print(os.listdir(ROOT))
# for i in ROOT.iterdir():
#     print(i, i.is_dir())

# for dirpath, dirs, files in os.walk(ROOT):
#     for _file in files:
#         print(Path(dirpath) / _file)

# for i in PHOTO_PATH.glob("**/*.jpg"): -> itereaza si sub-directoare

count = 0
for i in PHOTO_PATH.glob("*.jpg"):
    i.rename(PHOTO_PATH / f"Andreea&Andrei-{count}.jpg")
    count += 1