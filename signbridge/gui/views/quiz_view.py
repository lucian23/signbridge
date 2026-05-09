"""Quiz game view."""
import tkinter as tk
from tkinter import messagebox
from signbridge.modules.lesson_manager import LessonManager
from signbridge.modules.progress_tracker import ProgressTracker

class QuizView(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, bg='#f1f5f9', **kw)
        tk.Label(self, text='Quiz LSR', font=('Segoe UI', 22, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(anchor='w', padx=32, pady=(24,16))
        self.lm = LessonManager()
        self.pt = ProgressTracker()
        self.questions = []
        self.current = 0
        self.score = 0
        self._build_start()

    def _build_start(self):
        self.start_frame = tk.Frame(self, bg='#f1f5f9')
        self.start_frame.pack(fill='both', expand=True, padx=32, pady=8)
        tk.Label(self.start_frame, text='Alege categoria:', font=('Segoe UI', 14), bg='#f1f5f9').pack(pady=16)
        self.cat_var = tk.StringVar(value='Toate')
        tk.Radiobutton(self.start_frame, text='Toate', variable=self.cat_var, value='Toate', bg='#f1f5f9').pack()
        for cat in ['Salutari', 'Familie', 'Mancare', 'Numere', 'Urgente']:
            tk.Radiobutton(self.start_frame, text=cat, variable=self.cat_var, value=cat, bg='#f1f5f9').pack()
        tk.Button(self.start_frame, text='Start Quiz', command=self._start, bg='#3b82f6', fg='white', font=('Segoe UI', 12, 'bold')).pack(pady=24)

    def _start(self):
        cat = self.cat_var.get()
        cat = None if cat == 'Toate' else cat
        self.questions = self.lm.generate_quiz(category=cat, count=5)
        self.current = 0
        self.score = 0
        self.start_frame.destroy()
        self._show_question()

    def _show_question(self):
        if self.current >= len(self.questions):
            self._show_result()
            return
        q = self.questions[self.current]
        self.q_frame = tk.Frame(self, bg='#f1f5f9')
        self.q_frame.pack(fill='both', expand=True, padx=32, pady=8)
        tk.Label(self.q_frame, text=f"Intrebare {self.current+1}/{len(self.questions)}", font=('Segoe UI', 12), bg='#f1f5f9', fg='#64748b').pack(pady=8)
        tk.Label(self.q_frame, text=f"Semnul pentru: {q['description']}", font=('Segoe UI', 18, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(pady=16)
        for opt in q['options']:
            tk.Button(self.q_frame, text=opt, command=lambda o=opt: self._answer(o, q), bg='#e2e8f0', fg='#0f172a', font=('Segoe UI', 12), width=20).pack(pady=4)

    def _answer(self, selected, question):
        correct = selected == question['correct']
        if correct:
            self.score += 1
        self.pt.record_attempt(question['sign_id'], correct)
        self.q_frame.destroy()
        self.current += 1
        self._show_question()

    def _show_result(self):
        tk.Label(self, text='Quiz completat!', font=('Segoe UI', 22, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(pady=24)
        pct = round(self.score / len(self.questions) * 100)
        tk.Label(self, text=f"Scor: {self.score}/{len(self.questions)} ({pct}%)", font=('Segoe UI', 16), bg='#f1f5f9', fg='#3b82f6').pack(pady=8)
        tk.Button(self, text='Reia Quiz', command=self._restart, bg='#3b82f6', fg='white', font=('Segoe UI', 12, 'bold')).pack(pady=16)

    def _restart(self):
        for w in list(self.winfo_children()):
            w.destroy()
        self._build_start()
