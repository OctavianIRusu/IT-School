import.sqlite3
from pathlib import Path

class Database:
    
    def __init__(self, db_file_path: Path, create_table_query: str) -> None:
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()
        self.create_table_query = create_table_query
        
        # executati o metoda care creeaza tabelul pe baza querry-ului daca el nu exista
        
    def read_all(self):
        rows = self.cursor.execute("""SELECT * FROM ?;""", (self.create_table_query)) # numele tabelului se extrage din query de creare tabel
        return rows.fetchall()
    
    
    # def create(self, name, tel)
    
    # def update
    
    # def delete
    
class ContactsDb: