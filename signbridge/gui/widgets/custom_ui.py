"""Custom UI widgets for SignBridge."""
import tkinter as tk

class GlassCard(tk.Canvas):
    def __init__(self, master, width=280, height=160, bgcol='#1e293b', **kw):
        super().__init__(master, width=width, height=height, bg=bgcol, highlightthickness=0, **kw)
        self._gw, self._gh = width, height
        self._bgcol = bgcol
        self._hover = False
        self.bind('<Enter>', lambda e: self._on_hover(True))
        self.bind('<Leave>', lambda e: self._on_hover(False))
        self.after(50, self._draw)

    def _draw(self):
        self.delete('all')
        for i in range(self._gh):
            ratio = i / self._gh
            r = int(15 + ratio * 10)
            g = int(41 + ratio * 15)
            b = int(59 + ratio * 15)
            self.create_line(0, i, self._gw, i, fill=f'#{r:02x}{g:02x}{b:02x}')
        self.create_rounded_rect(2, 2, self._gw-2, self._gh-2, 16, outline='#3b82f6' if self._hover else '#334155', width=2 if self._hover else 1)

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kw):
        points = []
        r = radius
        points += [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2, x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1]
        return self.create_polygon(points, smooth=True, **kw)

    def _on_hover(self, state):
        self._hover = state
        self._draw()

class NavButton(tk.Frame):
    def __init__(self, master, text, icon='●', command=None, active=False, **kw):
        super().__init__(master, bg='#0f172a', **kw)
        self.command = command
        self.active = active
        self.icon_lbl = tk.Label(self, text=icon, font=('Segoe UI', 12), bg='#0f172a', fg='#3b82f6' if active else '#64748b')
        self.icon_lbl.pack(side='left', padx=(16,8))
        self.text_lbl = tk.Label(self, text=text, font=('Segoe UI', 11, 'bold' if active else 'normal'), bg='#0f172a', fg='#f8fafc' if active else '#94a3b8')
        self.text_lbl.pack(side='left')
        self.indicator = tk.Frame(self, width=3, bg='#3b82f6' if active else '#0f172a')
        self.indicator.pack(side='left', fill='y', padx=(8,0))
        self.bind('<Enter>', lambda e: self._hover(True))
        self.bind('<Leave>', lambda e: self._hover(False))
        self.bind('<Button-1>', lambda e: command() if command else None)
        for w in [self.icon_lbl, self.text_lbl]:
            w.bind('<Button-1>', lambda e: command() if command else None)

    def _hover(self, state):
        if not self.active:
            self.text_lbl.config(fg='#cbd5e1' if state else '#94a3b8')
            self.icon_lbl.config(fg='#60a5fa' if state else '#64748b')

    def set_active(self, active):
        self.active = active
        self.text_lbl.config(fg='#f8fafc' if active else '#94a3b8', font=('Segoe UI', 11, 'bold' if active else 'normal'))
        self.icon_lbl.config(fg='#3b82f6' if active else '#64748b')
        self.indicator.config(bg='#3b82f6' if active else '#0f172a')
