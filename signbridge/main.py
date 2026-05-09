import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
import ttkbootstrap as ttkb
from signbridge.gui.views.main_window import MainApp

if __name__ == '__main__':
    root = ttkb.Window(themename='flatly')
    app = MainApp(root)
    root.mainloop()
