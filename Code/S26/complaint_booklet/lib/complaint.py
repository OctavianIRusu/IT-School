from typing import List
from pathlib import Path
from typing import List
import json

class Complaint:

    current_id = 0

    def __init__(self, title, text) -> None:
        self.__id = Complaint.current_id
        self.__title = title
        self.__text = text
        self.__resolved = False

        Complaint.current_id += 1

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    @property
    def title(self):
        return self.__title

    @property
    def resolved(self):
        return self.__resolved

    def mark_as_resolved(self):
        self.__resolved = True

    def __str__(self) -> str:
        return f"Title: {self.title}\nText: {self.text}"


class Booklet:

    def __init__(self) -> None:
        self.__complaints: List[Complaint] = []

    @property
    def complaints(self):
        return self.__complaints

    @property
    def unsolved_complaints(self):
        return [x for x in self.__complaints if not x.resolved]

    def add(self, complaint: Complaint):
        self.__complaints.append(complaint)

    def mark_solved(self, id: int):
        for i in self.__complaints:
            if id == i.id:
                i.mark_as_resolved()

    def __len__(self):
        return len(self.__complaints)

    def load_json(self, file_path: Path) -> List(Complaint):
        """
        Raises:
        OSError: if the path is not accessible
        json.JSONDecodeError: if json can not be parsed
        """
        with open(self.__data_store_path, "r") as fin:
            objects = json.load(fin)
        return objects

    def save_json(self, file_path: Path):
        with open(file_path, "w") as fout: