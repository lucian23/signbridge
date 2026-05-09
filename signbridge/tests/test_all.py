import pytest, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from signbridge.core.config import ConfigManager
from signbridge.core.database import DatabaseManager
from signbridge.modules.sign_manager import SignManager
from signbridge.modules.lesson_manager import LessonManager
from signbridge.modules.progress_tracker import ProgressTracker

@pytest.fixture(autouse=True)
def reset():
    ConfigManager._instance = None
    DatabaseManager._instance = None
    yield
    ConfigManager._instance = None
    DatabaseManager._instance = None

class TestConfig:
    def test_singleton(self):
        c1 = ConfigManager()
        c2 = ConfigManager()
        assert c1 is c2

    def test_defaults(self):
        c = ConfigManager()
        assert c.get('theme') == 'flatly'

class TestDatabase:
    def test_seed(self):
        db = DatabaseManager()
        s = db.execute('SELECT COUNT(*) FROM signs').fetchone()[0]
        assert s >= 22
        l = db.execute('SELECT COUNT(*) FROM lessons').fetchone()[0]
        assert l >= 5

class TestSignManager:
    def test_list(self):
        sm = SignManager()
        signs = sm.list_signs()
        assert len(signs) >= 22
        assert any(s['word'] == 'Salut' for s in signs)

    def test_by_category(self):
        sm = SignManager()
        signs = sm.list_signs(category='Urgente')
        assert len(signs) >= 3

    def test_search(self):
        sm = SignManager()
        r = sm.search_by_word('Sal')
        assert len(r) >= 1

class TestLessonManager:
    def test_list(self):
        lm = LessonManager()
        lessons = lm.list_lessons()
        assert len(lessons) >= 5

    def test_get_signs(self):
        lm = LessonManager()
        signs = lm.get_lesson_signs(1)
        assert len(signs) >= 3

    def test_quiz(self):
        lm = LessonManager()
        quiz = lm.generate_quiz(count=3)
        assert len(quiz) == 3
        assert 'options' in quiz[0]

class TestProgress:
    def test_record(self):
        pt = ProgressTracker()
        sm = SignManager()
        signs = sm.list_signs()
        if signs:
            pt.record_attempt(signs[0]['id'], True)
            stats = pt.get_stats()
            assert len(stats) >= 1
