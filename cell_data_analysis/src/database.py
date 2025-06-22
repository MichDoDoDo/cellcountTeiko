import sqlite3

def InitDB(conn):
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS samples (
        sample_id TEXT PRIMARY KEY,
        project TEXT,
        subject TEXT,
        condition TEXT,
        age INTEGER,
        sex TEXT,
        treatment TEXT,
        response TEXT,
        sample TEXT UNIQUE,
        sample_type TEXT,
        time_from_treatment_start INTEGER
    )
    """) 
    conn.commit()
    
def InitSampleData(conn):
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS celldata(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sample_id TEXT,
        population TEXT, 
        count INTEGER,
        FOREIGN KEY (sample_id) REFERENCES samples(sample_id) ON DELETE CASCADE
        )
        """)
    conn.commit()

def InitFrqDB(conn):
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS frequencies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sample_id TEXT,
        total_count INTEGER
        population TEXT,
        count INTEGER,
        percentage REAL,
        FOREIGN KEY (sample_id) REFERENCES samples(sample_id) ON DELETE CASCADE
    )
    """)
    conn.commit()
    