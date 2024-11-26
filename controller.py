import time
import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE experience_planning (
    planning_id INTEGER PRIMARY KEY AUTOINCREMENT,
    experience_id INTEGER,
    experience_type TEXT NOT NULL, -- 'growth' or 'general'
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    budget DECIMAL(10,2),
    status TEXT DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (experience_id) REFERENCES experiences(experience_id)
    );
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()
    
if __name__=="__main__":
    createDB()
    createTable()