"""SQLite database for LSR signs."""
import sqlite3, os

class DatabaseManager:
    _instance = None
    DB_PATH = os.path.expanduser('~/.signbridge/signbridge.db')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_db()
        return cls._instance

    def _init_db(self):
        os.makedirs(os.path.dirname(self.DB_PATH), exist_ok=True)
        self.conn = sqlite3.connect(self.DB_PATH, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS signs (
                id INTEGER PRIMARY KEY, word TEXT, category TEXT,
                gif_path TEXT, description TEXT, difficulty INTEGER
            );
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY, sign_id INTEGER, correct INTEGER,
                attempts INTEGER, last_date TEXT
            );
            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY, title TEXT, category TEXT,
                sign_ids TEXT, difficulty INTEGER
            );
        """)
        self.conn.commit()
        self._seed()

    def _seed(self):
        c = self.conn.execute("SELECT COUNT(*) FROM signs").fetchone()[0]
        if c == 0:
            signs = [
                ("Salut", "Salutari", "", "Mana ridicata la tampla", 1),
                ("Multumesc", "Salutari", "", "Mana la buze", 1),
                ("Da", "Raspunsuri", "", "Cap inclinat", 1),
                ("Nu", "Raspunsuri", "", "Cap dat pe spate", 1),
                ("Mama", "Familie", "", "Mana pe barbie", 1),
                ("Tata", "Familie", "", "Mana pe frunte", 1),
                ("Copil", "Familie", "", "Mana jos", 1),
                ("Mere", "Mancare", "", "Mana rotunda", 2),
                ("Paine", "Mancare", "", "Taiere", 2),
                ("Apa", "Mancare", "", "Mana la gura", 2),
                ("Scoala", "Locuri", "", "Mana pe palma", 2),
                ("Casa", "Locuri", "", "Acoperis", 2),
                ("Medic", "Urgente", "", "Mana la inima", 3),
                ("Durere", "Urgente", "", "Fata stramba", 3),
                ("Ajutor", "Urgente", "", "Ambele maini", 3),
                ("0", "Numere", "", "Pumn", 1),
                ("1", "Numere", "", "Deget aratator", 1),
                ("2", "Numere", "", "Doua degete", 1),
                ("3", "Numere", "", "Trei degete", 1),
                ("5", "Numere", "", "Cinci degete", 1),
                ("10", "Numere", "", "Mana deschisa", 2),
                ("100", "Numere", "", "Ambele maini", 3),
            ]
            self.conn.executemany(
                "INSERT INTO signs (word,category,gif_path,description,difficulty) VALUES (?,?,?,?,?)",
                signs
            )
            lessons = [
                ("Saluturi de baza", "Salutari", "1,2,3,4", 1),
                ("Familia mea", "Familie", "5,6,7", 1),
                ("La masa", "Mancare", "8,9,10", 2),
                ("Numere simple", "Numere", "16,17,18,19,20", 1),
                ("Urgente", "Urgente", "13,14,15", 3),
            ]
            self.conn.executemany(
                "INSERT INTO lessons (title,category,sign_ids,difficulty) VALUES (?,?,?,?)",
                lessons
            )
            self.conn.commit()

    def execute(self, sql, params=()):
        return self.conn.execute(sql, params)

    def commit(self):
        self.conn.commit()

DatabaseManager._instance = None
