import sys
from pathlib import Path

ROOT = Path(__file__).parent


def fibonacci():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


output_path = ROOT / "output"

try:
    output_path.mkdir(exist_ok=True)
except:
    print("Could not create output dir.")
    sys.exit(1)

fibonacci_gen = fibonacci()

for i in range(1, 101):
    file_path = output_path / f"{i}.txt"
    try:
        with file_path.open("w") as fout:
            fout.write(str(next(fibonacci_gen)))
    except OSError as err:
        print(err)
