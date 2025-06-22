import sqlite3 
from src.db_controller import DBController
from src.database import InitDB, InitSampleData, InitFrqDB

class CellDataRepo:
    
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.dbcon = DBController()
        InitDB(self.conn)

    def LoadData(self, path):
        InitSampleData(self.conn)
        InitFrqDB(self.conn)
        self.dbcon.LoadDataToDB(path, self.conn)
        self.dbcon.LoadFrqData(self.conn)

    def AddData(self, path):
        return self.dbcon.AddDataToDB(path, self.conn)
        
    def RemoveData(self, sampleId):
        if(self.dbcon.RemoveSampleFromDB(sampleId, self.conn)):
            print(f"removed {sampleId} from db")
            return True
        return False
        
    
