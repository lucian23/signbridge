"""Lesson and quiz management."""
from signbridge.core.database import DatabaseManager
import random

class LessonManager:
    def __init__(self):
        self.db = DatabaseManager()

    def list_lessons(self):
        rows = self.db.execute("SELECT * FROM lessons ORDER BY difficulty").fetchall()
        return [dict(r) for r in rows]

    def get_lesson_signs(self, lesson_id):
        row = self.db.execute("SELECT sign_ids FROM lessons WHERE id=?", (lesson_id,)).fetchone()
        if not row:
            return []
        ids = [int(x.strip()) for x in row[0].split(",")]
        signs = []
        for sid in ids:
            s = self.db.execute("SELECT * FROM signs WHERE id=?", (sid,)).fetchone()
            if s:
                signs.append(dict(s))
        return signs

    def generate_quiz(self, category=None, count=5):
        sql = "SELECT * FROM signs WHERE 1=1"
        params = []
        if category:
            sql += " AND category=?"
            params.append(category)
        sql += " ORDER BY RANDOM() LIMIT ?"
        params.append(count)
        rows = self.db.execute(sql, params).fetchall()
        quiz = []
        for r in rows:
            # Generate 3 wrong options from same category
            wrong = self.db.execute(
                "SELECT word FROM signs WHERE id!=? AND category=? ORDER BY RANDOM() LIMIT 3",
                (r["id"], r["category"])
            ).fetchall()
            options = [r["word"]] + [w[0] for w in wrong]
            random.shuffle(options)
            quiz.append({
                "sign_id": r["id"],
                "word": r["word"],
                "description": r["description"],
                "options": options,
                "correct": r["word"]
            })
        return quiz
