#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class CapstoneGuiApp:
    def __init__(self, master=None):
        # build ui
        self.Toplevel_01 = tk.Tk() if master is None else tk.Toplevel(master)
        self.Toplevel_01.configure(height=200, width=200)
        # First object created
        self.setup_ttk_styles(self.Toplevel_01)

        self.Labelframe_03 = ttk.Labelframe(self.Toplevel_01)
        self.Labelframe_03.configure(height=200, text='Console Log', width=200)
        scrollbar2 = ttk.Scrollbar(self.Labelframe_03)
        scrollbar2.configure(orient="vertical")
        scrollbar2.grid(column=1, padx="0 6", pady=6, row=0, sticky="ns")
        text1 = tk.Text(self.Labelframe_03)
        text1.configure(height=10, width=50)
        text1.grid(column=0, row=0)
        self.Labelframe_03.grid(padx=6, pady=6)

        # Main widget
        self.mainwindow = self.Toplevel_01

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = CapstoneGuiApp()
    app.run()
