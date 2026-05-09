"""Main window for SignBridge."""
import tkinter as tk
import ttkbootstrap as ttkb
from signbridge.gui.widgets.custom_ui import NavButton
from signbridge.gui.views.dashboard_view import DashboardView
from signbridge.gui.views.dictionary_view import DictionaryView
from signbridge.gui.views.lessons_view import LessonsView
from signbridge.gui.views.quiz_view import QuizView
from signbridge.gui.views.progress_view import ProgressView

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('SignBridge — Invata limbajul semnelor romanesc')
        self.root.geometry('1200x750')
        self.root.minsize(1000, 650)
        self.style = ttkb.Style('flatly')
        self._build_ui()

    def _build_ui(self):
        self.sidebar = tk.Frame(self.root, width=220, bg='#0f172a')
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)
        tk.Label(self.sidebar, text='SignBridge', font=('Segoe UI', 18, 'bold'), bg='#0f172a', fg='#f8fafc').pack(pady=(24,8), padx=20, anchor='w')
        tk.Label(self.sidebar, text='v1.0.0', font=('Segoe UI', 9), bg='#0f172a', fg='#64748b').pack(padx=20, anchor='w')
        tk.Frame(self.sidebar, height=2, bg='#1e293b').pack(fill='x', padx=16, pady=12)

        self.nav_buttons = []
        pages = [
            ('Panou Principal', '◈', self._show_dashboard),
            ('Dictionar', '☰', self._show_dictionary),
            ('Lectii', '▶', self._show_lessons),
            ('Quiz', '?', self._show_quiz),
            ('Progres', '◆', self._show_progress),
        ]
        for text, icon, cmd in pages:
            btn = NavButton(self.sidebar, text=text, icon=icon, command=cmd)
            btn.pack(fill='x', pady=2, padx=8)
            self.nav_buttons.append(btn)

        self.content = tk.Frame(self.root, bg='#f1f5f9')
        self.content.pack(side='right', fill='both', expand=True)
        self.views = {}
        self._show_dashboard()

    def _show_dashboard(self):
        self._activate_nav(0)
        self._clear_content()
        self.views['dashboard'] = DashboardView(self.content)
        self.views['dashboard'].pack(fill='both', expand=True)

    def _show_dictionary(self):
        self._activate_nav(1)
        self._clear_content()
        self.views['dictionary'] = DictionaryView(self.content)
        self.views['dictionary'].pack(fill='both', expand=True)

    def _show_lessons(self):
        self._activate_nav(2)
        self._clear_content()
        self.views['lessons'] = LessonsView(self.content)
        self.views['lessons'].pack(fill='both', expand=True)

    def _show_quiz(self):
        self._activate_nav(3)
        self._clear_content()
        self.views['quiz'] = QuizView(self.content)
        self.views['quiz'].pack(fill='both', expand=True)

    def _show_progress(self):
        self._activate_nav(4)
        self._clear_content()
        self.views['progress'] = ProgressView(self.content)
        self.views['progress'].pack(fill='both', expand=True)

    def _activate_nav(self, idx):
        for i, btn in enumerate(self.nav_buttons):
            btn.set_active(i == idx)

    def _clear_content(self):
        for w in list(self.content.winfo_children()):
            w.destroy()
