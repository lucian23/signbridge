"""Dictionary view."""
import tkinter as tk
from tkinter import ttk
from signbridge.modules.sign_manager import SignManager

class DictionaryView(tk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, bg='#f1f5f9', **kw)
        tk.Label(self, text='Dictionar LSR', font=('Segoe UI', 22, 'bold'), bg='#f1f5f9', fg='#0f172a').pack(anchor='w', padx=32, pady=(24,16))
        self.sm = SignManager()
        self._build_search()
        self._build_table()
        self._load()

    def _build_search(self):
        f = tk.Frame(self, bg='#f1f5f9')
        f.pack(fill='x', padx=32, pady=8)
        tk.Label(f, text='Cauta cuvant:', bg='#f1f5f9').pack(side='left')
        self.search_var = tk.StringVar()
        tk.Entry(f, textvariable=self.search_var, width=30).pack(side='left', padx=8)
        tk.Button(f, text='Cauta', command=self._search, bg='#3b82f6', fg='white').pack(side='left')
        self.cat_combo = ttk.Combobox(f, values=['Toate'] + self.sm.categories(), width=20, state='readonly')
        self.cat_combo.set('Toate')
        self.cat_combo.pack(side='left', padx=(16,0))
        self.cat_combo.bind('<<ComboboxSelected>>', lambda e: self._load())

    def _build_table(self):
        cols = ('word','category','description','difficulty')
        self.tree = ttk.Treeview(self, columns=cols, show='headings', height=16)
        for c in cols:
            self.tree.heading(c, text=c.capitalize())
            self.tree.column(c, width=180)
        self.tree.pack(fill='both', expand=True, padx=32, pady=8)

    def _load(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        cat = self.cat_combo.get()
        cat = None if cat == 'Toate' else cat
        for row in self.sm.list_signs(category=cat):
            self.tree.insert('', 'end', values=(row['word'], row['category'], row['description'], row['difficulty']))

    def _search(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in self.sm.search_by_word(self.search_var.get()):
            self.tree.insert('', 'end', values=(row['word'], row['category'], row['description'], row['difficulty']))
