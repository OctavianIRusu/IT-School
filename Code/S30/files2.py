from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent

FILE_PATH = ROOT / "code1.txt"

c_time = FILE_PATH.stat().st_ctime

c_date_time = datetime.fromtimestamp(c_time)

print(c_date_time)