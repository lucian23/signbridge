"""Progress view."""
import tkinter as tk
from tkinter import ttk
from signbridge.modules.progress_tracker import ProgressTracker

class ProgressView(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, bg='#f1f5f9', **kw)
        tk.Label(self, text='Progresul tau', font=('Segoe UI', 22, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(anchor='w', padx=32, pady=(24,16))
        self.pt = ProgressTracker()
        self._build_overall()
        self._build_table()

    def _build_overall(self):
        score = self.pt.overall_score()
        lbl = tk.Label(self, text=f"Scor general: {score}%", font=('Segoe UI', 24, 'bold'), bg='#f1f5f9', fg='#3b82f6')
        lbl.pack(anchor='w', padx=32, pady=8)

    def _build_table(self):
        cols = ('word','correct','attempts','rate')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=12)
        for c in cols:
            self.tree.heading(c, text=c.capitalize())
            self.tree.column(c, width=150)
        self.tree.pack(fill='both', expand=True, padx=32, pady=8)
        for row in self.pt.get_stats():
            self.tree.insert('', 'end', values=(row['word'], row['correct'], row['attempts'], f"{row['rate']:.0f}%"))
