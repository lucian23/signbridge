"""Manage LSR signs."""
from signbridge.core.database import DatabaseManager

class SignManager:
    def __init__(self):
        self.db = DatabaseManager()

    def list_signs(self, category=None, difficulty=None):
        sql = "SELECT * FROM signs WHERE 1=1"
        params = []
        if category:
            sql += " AND category=?"
            params.append(category)
        if difficulty is not None:
            sql += " AND difficulty=?"
            params.append(difficulty)
        sql += " ORDER BY difficulty, word"
        rows = self.db.execute(sql, params).fetchall()
        return [dict(r) for r in rows]

    def get_sign(self, sign_id):
        row = self.db.execute("SELECT * FROM signs WHERE id=?", (sign_id,)).fetchone()
        return dict(row) if row else None

    def search_by_word(self, word):
        rows = self.db.execute("SELECT * FROM signs WHERE word LIKE ?", (f"%{word}%",)).fetchall()
        return [dict(r) for r in rows]

    def categories(self):
        rows = self.db.execute("SELECT DISTINCT category FROM signs ORDER BY category").fetchall()
        return [r[0] for r in rows]
