#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class CapstoneGuiApp:
    def __init__(self, master=None):
        # build ui
        self.Toplevel_00 = tk.Tk() if master is None else tk.Toplevel(master)
        self.Toplevel_00.configure(height=200, width=200)
        # First object created
        self.setup_ttk_styles(self.Toplevel_00)

        self.frame_01 = ttk.Frame(self.Toplevel_00)
        self.frame_01.configure(padding=6, relief="sunken")
        self.Labelframe_01 = ttk.Labelframe(self.frame_01)
        self.Labelframe_01.configure(
            height=200, text='Reputation Range', width=200)
        self.Label_01 = ttk.Label(self.Labelframe_01)
        self.Label_01.configure(text='Less than 0')
        self.Label_01.grid(column=0, row=0)
        self.Label_02 = ttk.Label(self.Labelframe_01)
        self.Label_02.configure(text='0-100')
        self.Label_02.grid(column=0, row=1)
        self.Label_03 = ttk.Label(self.Labelframe_01)
        self.Label_03.configure(text='More than 100')
        self.Label_03.grid(column=0, row=2)
        self.Labelframe_01.grid(column=0, padx=6, pady=6, row=0, sticky="ew")
        self.Labelframe_02 = ttk.Labelframe(self.frame_01)
        self.Labelframe_02.configure(height=200, text='File Count', width=200)
        self.Label_04 = ttk.Label(self.Labelframe_02)
        self.Label_04.configure(text='...')
        self.Label_04.grid(column=0, row=0)
        self.Label_05 = ttk.Label(self.Labelframe_02)
        self.Label_05.configure(text='...')
        self.Label_05.grid(column=0, row=1)
        self.Label_06 = ttk.Label(self.Labelframe_02)
        self.Label_06.configure(text='...')
        self.Label_06.grid(column=0, row=2)
        self.Labelframe_02.grid(column=1, padx=6, row=0, sticky="ew")
        self.Frame_02 = ttk.Frame(self.frame_01)
        self.Frame_02.configure(height=200, width=200)
        self.Entry_01 = ttk.Entry(self.Frame_02)
        self.Entry_01.grid(column=1, padx=6, row=0)
        self.Label_07 = ttk.Label(self.Frame_02)
        self.Label_07.configure(text='Filepath Filter')
        self.Label_07.grid(column=0, row=0)
        self.Button_01 = ttk.Button(self.Frame_02)
        self.filter_var = tk.StringVar(value='Filter')
        self.Button_01.configure(text='Filter', textvariable=self.filter_var)
        self.Button_01.grid(column=2, row=0)
        self.Frame_02.grid(column=1, padx=6, row=1, sticky="e")
        self.Frame_03 = ttk.Frame(self.frame_01)
        self.Frame_03.configure(height=200, width=200)
        self.Button_02 = ttk.Button(self.Frame_03)
        self.Button_02.configure(text='Visit VirusTotal Webpage')
        self.Button_02.grid(column=1, padx=6, row=0)
        self.Label_11 = ttk.Label(self.Frame_03)
        self.Label_11.configure(text='Select Hash from Table:')
        self.Label_11.grid(column=0, row=0)
        self.Frame_03.grid(column=0, padx=6, row=1, sticky="w")
        self.treeview_01 = ttk.Treeview(self.frame_01)
        self.treeview_01.configure(height=20, selectmode="extended", show="headings", yscrollcommand="{"name": "yscrollcommand", "type": "command", "cbtype": "scrollset", "value": "treeview_yscroll"}")
        self.treeview_01_cols = [
            'column_01',
            'column_02',
            'column_03',
            'column_04']
        self.treeview_01_dcols = [
            'column_01',
            'column_02',
            'column_03',
            'column_04']
        self.treeview_01.configure(
            columns=self.treeview_01_cols,
            displaycolumns=self.treeview_01_dcols)
        self.treeview_01.column(
            "column_01",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview_01.column(
            "column_02",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview_01.column(
            "column_03",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview_01.column(
            "column_04",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview_01.heading("column_01", anchor="w", text='Hash')
        self.treeview_01.heading(
            "column_02",
            anchor="w",
            text='VirustTotal Reputation')
        self.treeview_01.heading(
            "column_03",
            anchor="w",
            text='Age (First Submitted)')
        self.treeview_01.heading("column_04", anchor="w", text='Filepath')
        self.treeview_01.grid(column=0, columnspan=2, padx="6 0", row=2)
        self.Scrollbar_01 = ttk.Scrollbar(self.frame_01)
        self.Scrollbar_01.configure(orient="vertical")
        self.Scrollbar_01.grid(
            column=3,
            padx="0 6",
            pady=6,
            row=2,
            sticky="ns")
        self.Scrollbar_01.configure(command=self.yview)
        self.frame_01.grid(column=0, row=0)
        self.frame_01.rowconfigure(0, weight=1)
        self.frame_01.rowconfigure("all", weight=1)
        self.frame_01.columnconfigure(0, weight=1)
        self.frame_01.columnconfigure("all", weight=1)
        self.Toplevel_00.rowconfigure("all", weight=1)
        self.Toplevel_00.columnconfigure("all", weight=1)

        # Main widget
        self.mainwindow = self.Toplevel_00
        # Main menu
        _main_menu = self.create_Menu_01(self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)

    def run(self):
        self.mainwindow.mainloop()

    def create_Menu_01(self, master):
        self.Menu_01 = tk.Menu(master)
        self.Menu_01.configure(tearoff=False, title='test')
        self.Submenu_00 = tk.Menu(self.Menu_01, tearoff=False)
        self.Menu_01.add(
            tk.CASCADE,
            menu=self.Submenu_00,
            label='Cache Commands (Advanced)')
        self.Submenu_00.add("command", label='Update Local Cache')
        self.Submenu_00.add("command", label='Update VirusTotal Cache')
        self.Menu_01.add("command", label='Show Console Logs')
        return self.Menu_01

    def yview(self, mode=None, value=None, units=None):
        pass


if __name__ == "__main__":
    app = CapstoneGuiApp()
    app.run()
