"""Track user progress."""
from signbridge.core.database import DatabaseManager
import datetime

class ProgressTracker:
    def __init__(self):
        self.db = DatabaseManager()

    def record_attempt(self, sign_id, correct):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        row = self.db.execute(
            "SELECT * FROM progress WHERE sign_id=?", (sign_id,)
        ).fetchone()
        if row:
            new_attempts = row["attempts"] + 1
            new_correct = row["correct"] + (1 if correct else 0)
            self.db.execute(
                "UPDATE progress SET correct=?, attempts=?, last_date=? WHERE sign_id=?",
                (new_correct, new_attempts, date, sign_id)
            )
        else:
            self.db.execute(
                "INSERT INTO progress (sign_id, correct, attempts, last_date) VALUES (?,?,?,?)",
                (sign_id, 1 if correct else 0, 1, date)
            )
        self.db.commit()

    def get_stats(self):
        rows = self.db.execute("""
            SELECT s.word, p.correct, p.attempts,
                   CAST(p.correct AS REAL)/p.attempts*100 as rate
            FROM progress p JOIN signs s ON p.sign_id=s.id
            ORDER BY rate DESC
        """).fetchall()
        return [dict(r) for r in rows]

    def overall_score(self):
        row = self.db.execute("""
            SELECT SUM(correct) as total_correct, SUM(attempts) as total_attempts
            FROM progress
        """).fetchone()
        if not row or not row["total_attempts"]:
            return 0
        return round(row["total_correct"] / row["total_attempts"] * 100, 1)
