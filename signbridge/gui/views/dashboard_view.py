"""Dashboard for SignBridge."""
import tkinter as tk
from signbridge.gui.widgets.custom_ui import GlassCard
from signbridge.modules.sign_manager import SignManager
from signbridge.modules.progress_tracker import ProgressTracker
from signbridge.modules.lesson_manager import LessonManager

class DashboardView(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, bg='#f1f5f9', **kw)
        tk.Label(self, text='SignBridge', font=('Segoe UI', 22, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(anchor='w', padx=32, pady=(24,16))
        tk.Label(self, text='Invata limbajul semnelor romanesc (LSR) pas cu pas.', font=('Segoe UI', 12), bg='#f1f5f9', fg='#64748b').pack(anchor='w', padx=32, pady=(0,16))
        cards_frame = tk.Frame(self, bg='#f1f5f9')
        cards_frame.pack(fill='x', padx=32, pady=8)
        sm = SignManager()
        pt = ProgressTracker()
        lm = LessonManager()
        total_signs = len(sm.list_signs())
        total_lessons = len(lm.list_lessons())
        score = pt.overall_score()
        cards = [
            (str(total_signs), 'Semne in baza de date', '#3b82f6'),
            (str(total_lessons), 'Lectii disponibile', '#10b981'),
            (f'{score}%', 'Scorul tau general', '#f59e0b'),
        ]
        for val, lbl, color in cards:
            c = GlassCard(cards_frame, width=260, height=120, bgcol='#ffffff')
            c.create_text(130, 40, text=val, font=('Segoe UI', 28, 'bold'), fill=color, anchor='center')
            c.create_text(130, 85, text=lbl, font=('Segoe UI', 11), fill='#64748b', anchor='center')
            c.pack(side='left', padx=(0,16))
