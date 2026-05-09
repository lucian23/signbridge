"""Lessons view."""
import tkinter as tk
from tkinter import ttk
from signbridge.modules.lesson_manager import LessonManager

class LessonsView(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, bg='#f1f5f9', **kw)
        tk.Label(self, text='Lectii LSR', font=('Segoe UI', 22, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(anchor='w', padx=32, pady=(24,16))
        self.lm = LessonManager()
        self._build_list()

    def _build_list(self):
        self.lesson_frame = tk.Frame(self, bg='#f1f5f9')
        self.lesson_frame.pack(fill='both', expand=True, padx=32, pady=8)
        for lesson in self.lm.list_lessons():
            frame = tk.Frame(self.lesson_frame, bg='#ffffff', bd=1, relief='solid')
            frame.pack(fill='x', pady=4)
            tk.Label(frame, text=lesson['title'], font=('Segoe UI', 14, 'bold'), bg='#ffffff', fg='#0f172a').pack(anchor='w', padx=16, pady=(8,0))
            tk.Label(frame, text=f"Categorie: {lesson['category']} | Dificultate: {lesson['difficulty']}", font=('Segoe UI', 10), bg='#ffffff', fg='#64748b').pack(anchor='w', padx=16, pady=(0,8))
            signs = self.lm.get_lesson_signs(lesson['id'])
            words = ', '.join([s['word'] for s in signs])
            tk.Label(frame, text=f"Semne: {words}", font=('Segoe UI', 10), bg='#ffffff', fg='#334155').pack(anchor='w', padx=16, pady=(0,8))
