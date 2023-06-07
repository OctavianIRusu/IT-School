# https://pypdf2.readthedocs.io/en/latest/user/extract-text.html
# https://docs.reportlab.com/
# https://docs.reportlab.com/preppy/

from PyPDF2 import PdfReader
from pathlib import Path

ROOT = Path(__file__).parent
PDF_PATH = ROOT / "Tom_Sawyer.pdf"

reader = PdfReader(PDF_PATH)
page = reader.pages[5]

# print(page.extract_text())

for page in reader.pages:
    print(page.extract_text)