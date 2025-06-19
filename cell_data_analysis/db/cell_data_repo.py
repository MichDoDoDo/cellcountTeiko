import sqlite3 
from src.db_controller import DBController

class CellDataRepo:
    
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.init_db()

    def load_data(self, path):
        DBController.load_data_to_db(path, self.conn)

    def init_db (self):
        dbcon = self.conn.cursor()
        dbcon.execute('''
        CREATE TABLE IF NOT EXISTS samples (
            sample_id TEXT PRIMARY KEY,
            indication TEXT,
            treatment TEXT,
            time_from_treatment_start INTEGER,
            response TEXT,
            gender TEXT,
            b_cell INTEGER,
            cd8_t_cell INTEGER,
            cd4_t_cell INTEGER,
            nk_cell INTEGER,
            monocyte INTEGER)''')
        self.conn.commit()
    
    #todo: add analysis