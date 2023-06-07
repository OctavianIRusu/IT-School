from pathlib import Path
from typing import List
import json

from lib.complaint import Complaint, Booklet

def load_json(file_path: Path) -> List(Complaint):
    """
    Raises:
        OSError: if the path is not accessible
        json.JSONDecodeError: if json can not be parsed
        """
    with open(file_path, "r") as fin:
        objects = json.load(fin)
    return objects

def save_json(file_path: Path, book: Booklet):
    with open(file_path, "w") as fout: