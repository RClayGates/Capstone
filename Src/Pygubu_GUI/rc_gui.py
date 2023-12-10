#!/usr/bin/python3
# imports: std
import threading
import tkinter as tk
from tkinter import ttk
from datetime import datetime


# imports: non-std

# imports: local
from rc_logger import src_log

# constants


# main()
def main():
    # app = CapstoneGuiAppTL_00(
    #     local_cache=test_local_cache,
    #     vt_cache=test_vt_cache,
    #     # startup=test_startup,
    #     # treeview_01=test_treeview, # TODO: Need to figure how out to insert exterior function properly
    #     button_01=test_button,
    #     button_02=test_button,
    # )
    # app.run()
    pass


class CapstoneGuiAppTL_00:
    def __init__(self, *args, master=None, **kwargs):
        self.args = args
        self.kwargs = kwargs

        # build ui
        self.Toplevel_00 = tk.Tk() if master is None else tk.Toplevel(master)
        self.Toplevel_00.title("Capstone")
        self.Toplevel_00.resizable(False, False)
        # Initial Boot up ---V
        self.data_loaded = tk.IntVar(value=0)
        # TODO: work on a good startup implementation that doesn't leave the user waiting for ui
        # self.__local_cache = self.kwargs.get('local_cache')()
        # self.__vt_cache = self.kwargs.get('vt_cache')()
        # self.__local_cache = {'test': {'filepath': 'Directory'}}
        # self.__vt_cache = {'test': {'data': {'attributes': {'reputation': 0}}}}

        # def startup(_self):
        #     if not _self.data_loaded.get():
        #         _self.__local_cache = self.kwargs.get("local_cache")()
        #         _self.__vt_cache = self.kwargs.get("vt_cache")()
        #         _self.data_loaded.set(value=1)
        #         return _self

        # self.Toplevel_00.bind(
        #     "<Visibility>", lambda event: self.startup(event))

        # Initial Boot up ---^
        #
        # First object created
        # self.setup_ttk_styles(self.Toplevel_00) <- commented rather than deleted (reason: unsure why generated)
        #
        # Tl_00
        self.Frame_01 = ttk.Frame(self.Toplevel_00)
        # self.Frame_01.bind("<>", lambda event: print(event))
        self.Frame_01.configure(padding=6, relief="sunken")
        #
        # Tl_00:F_01
        self.Labelframe_01 = ttk.Labelframe(self.Frame_01)
        self.Labelframe_01.configure(height=200, text="Reputation Range", width=200)
        #
        # Tl_00:F_01:LF_01
        self.Label_01 = ttk.Label(self.Labelframe_01)
        self.Label_01.configure(text="Less than 0")
        self.Label_01.grid(column=0, row=0, sticky="w")
        # Tl_00:F_01:LF_01
        self.Label_02 = ttk.Label(self.Labelframe_01)
        self.Label_02.configure(text="0-100")
        self.Label_02.grid(column=0, row=1, sticky="w")
        # Tl_00:F_01:LF_01
        self.Label_03 = ttk.Label(self.Labelframe_01)
        self.Label_03.configure(text="More than 100")
        self.Label_03.grid(column=0, row=2, sticky="w")
        # Tl_00:F_01:LF_01
        self.Labelframe_01.grid(column=0, padx=6, pady=6, row=0, sticky="ew")
        #
        # Tl_00:F_01
        self.Labelframe_02 = ttk.Labelframe(self.Frame_01)
        self.Labelframe_02.configure(height=200, text="File Count", width=200)
        #
        # Tl_00:F_01:LF_02
        self.Label_04_var = tk.IntVar(value=0)
        self.Label_04 = ttk.Label(self.Labelframe_02)
        self.Label_04.configure(text="...", textvariable=self.Label_04_var)
        self.Label_04.grid(column=0, row=0)
        # Tl_00:F_01:LF_02
        self.Label_05_var = tk.IntVar(value=0)
        self.Label_05 = ttk.Label(self.Labelframe_02)
        self.Label_05.configure(text="...", textvariable=self.Label_05_var)
        self.Label_05.grid(column=0, row=1)
        # Tl_00:F_01:LF_02
        self.Label_06_var = tk.IntVar(value=0)
        self.Label_06 = ttk.Label(self.Labelframe_02)
        self.Label_06.configure(text="...", textvariable=self.Label_06_var)
        self.Label_06.grid(column=0, row=2)
        # Tl_00:F_01:LF_02
        self.Labelframe_02.grid(column=1, padx=6, row=0, sticky="ew")
        #
        # Tl_00:F_01
        # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
        # self.Frame_02 = ttk.Frame(self.Frame_01)
        # self.Frame_02.configure(height=200, width=200)
        #
        # Tl_00:F_01:F_02
        # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
        # self.Entry_01_var = tk.StringVar()
        # self.Entry_01 = ttk.Entry(self.Frame_02, textvariable=self.Entry_01_var)
        # self.Entry_01.grid(column=1, padx=6, row=0)
        # Tl_00:F_01:F_02
        # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
        # self.Label_07 = ttk.Label(self.Frame_02)
        # self.Label_07.configure(text="Filepath Filter")
        # self.Label_07.grid(column=0, row=0)

        # String Variable
        # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
        # self.filter_var = tk.StringVar(value="Filter")
        # Tl_00:F_01:F_02
        # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
        # self.Button_01 = ttk.Button(self.Frame_02, command=lambda: self.button_01())
        # self.Button_01.configure(text="Filter", textvariable=self.filter_var)
        # self.Button_01.grid(column=2, row=0)

        # Tl_00:F_01:F_02
        # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
        # self.Frame_02.grid(column=1, padx=6, row=1, sticky="e")
        #
        # Tl_00:F_01
        self.Frame_03 = ttk.Frame(self.Frame_01)
        self.Frame_03.configure(height=200, width=200)
        #
        # Tl_00:F_01:F_03
        self.Button_02 = ttk.Button(self.Frame_03, command=lambda: self.button_02())
        self.Button_02.configure(text="Visit VirusTotal Webpage")
        self.Button_02.grid(column=1, padx=6, row=0)
        # Tl_00:F_01:F_03
        self.Label_11 = ttk.Label(self.Frame_03)
        self.Label_11.configure(text="Select Hash from Table:")
        self.Label_11.grid(column=0, row=0)
        # Tl_00:F_01:F_03
        self.Frame_03.grid(column=0, padx=6, row=1, sticky="w")
        #
        # Tl_00:F_01
        self.treeview_01_var = tk.StringVar()
        self.treeview_01 = ttk.Treeview(self.Frame_01)
        # self.treeview_01.bind(
        #     "<<TreeviewSelect>>", lambda event: self.test_treeview_01_select(event)
        # )
        self.treeview_01.configure(
            # height=20,
            selectmode="extended",
            show="headings",
        )
        self.treeview_01_cols = ["column_01", "column_02", "column_03", "column_04"]
        self.treeview_01_dcols = ["column_01", "column_02", "column_03", "column_04"]
        self.treeview_01.configure(
            columns=self.treeview_01_cols, displaycolumns=self.treeview_01_dcols
        )
        self.treeview_01.column(
            "column_01", anchor="w", stretch=False, width=280, minwidth=40
        )
        self.treeview_01.column(
            "column_02", anchor="w", stretch=False, width=130, minwidth=40
        )
        self.treeview_01.column(
            "column_03", anchor="w", stretch=False, width=120, minwidth=40
        )
        self.treeview_01.column(
            "column_04", anchor="w", stretch=False, width=200, minwidth=40
        )
        self.treeview_01.heading("column_01", anchor="w", text="Hash")
        self.treeview_01.heading("column_02", anchor="w", text="VirustTotal Reputation")
        self.treeview_01.heading("column_03", anchor="w", text="Age (First Submitted)")
        self.treeview_01.heading("column_04", anchor="w", text="Filepath")
        # important treeview logic
        for args in self.test_treeview_01_insert():
            # print(args)
            self.treeview_01.insert(
                parent=args[0], index=args[1], values=args[2], tags="cn"
            )
        self.treeview_01.tag_configure("cn", font=("Courier", 10))
        self.treeview_01.grid(column=0, columnspan=2, padx="6 0", pady="6 0", row=2)
        # Tl_00: F_01 Scroll bar needs to be after target is initialised
        #           but before treeview.configure(yscrollcommand)
        self.Scrollbar_01 = ttk.Scrollbar(self.Frame_01)
        self.Scrollbar_01.configure(orient="vertical", command=self.treeview_01.yview)
        self.Scrollbar_01.grid(column=3, padx="0 6", pady=6, row=2, sticky="ns")
        self.Scrollbar_02 = ttk.Scrollbar(self.Frame_01)
        self.Scrollbar_02.configure(orient="horizontal", command=self.treeview_01.xview)
        self.Scrollbar_02.grid(
            column=0, columnspan=2, padx="6 0", pady="0 6", row=3, sticky="we"
        )
        self.treeview_01.configure(
            yscrollcommand=self.Scrollbar_01.set, xscrollcommand=self.Scrollbar_02.set
        )
        #
        # Tl_00:F_01
        self.Frame_01.grid(column=0, row=0)
        self.Frame_01.rowconfigure(0, weight=1)
        self.Frame_01.rowconfigure("all", weight=1)
        self.Frame_01.columnconfigure(0, weight=1)
        self.Frame_01.columnconfigure("all", weight=1)
        # Tl_00
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
        self.Menu_01.configure(tearoff=False, title="test")
        self.Submenu_00 = tk.Menu(self.Menu_01, tearoff=False)
        self.Menu_01.add(
            tk.CASCADE, menu=self.Submenu_00, label="Cache Commands (Advanced)"
        )
        # self.Submenu_00.add("command", label="Update Local Cache")
        # self.Submenu_00.add("command", label="Update VirusTotal Cache")
        self.Submenu_00.add_command(
            label="Update Local Cache", command=lambda: self.menu_01()
        )
        self.Submenu_00.add_command(
            label="Update VirusTotal Cache", command=lambda: self.menu_02()
        )
        # self.Menu_01.add("command", label="Show Console Logs")
        self.Menu_01.add_command(
            label="Show Console Logs", command=lambda: self.menu_03()
        )
        return self.Menu_01

    # def startup(self, event):
    # print(self.__local_cache, self.__vt_cache)
    # self.__local_cache['status'] = 'test'
    # pass
    # print(event)
    # if not self.data_loaded.get():
    #     self.__local_cache = self.kwargs.get("local_cache")()
    #     self.__vt_cache = self.kwargs.get("vt_cache")()
    #     self.data_loaded.set(value=1)
    #     return self
    # return self.kwargs.get("startup", False)()

    # TODO: FILTER IMPLEMENTATION Uncomment when filter functionality works
    # def button_01(self):
    #     table_filter = self.Entry_01_var.get()
    #     if len(table_filter) > 0:
    #         self.treeview_01.delete(
    #             *self.treeview_01.get_children()
    #         )  # using splat (*) to unpack get_children
    #     self.test_treeview_01_insert(_filter=table_filter)

    def button_02(self):
        for value in self.treeview_01.selection():
            if len(self.treeview_01.selection()) == 1:
                hashkey = self.treeview_01.item(value)["values"][0]
                src_log.debug(f"{hashkey = }")
                vt_id = self.vt_cache.get(hashkey)
                # src_log.debug(f"{vt_id = }")
                if vt_id:
                    vt_id = vt_id.get("data")
                    # src_log.debug(f"data: {vt_id = }")
                    if vt_id:
                        vt_id = vt_id.get("id")
                src_log.debug(f"key:data:{vt_id = }")
                self.kwargs.get("button_02")(_target_id=vt_id)

    def menu_01(self):
        self.new_win = tk.Toplevel()
        self.new_win.geometry("300x50")
        self.new_win.resizable(False, False)
        self.new_win.title("Processing")
        self.frame_10 = ttk.LabelFrame(self.new_win)
        self.frame_10.configure(text="Updating Local Cache", padding=6)
        self.frame_10.pack(fill="both", expand=True)
        self.progress = ttk.Progressbar(self.frame_10)
        self.progress.configure(orient="horizontal", mode="indeterminate")
        self.progress.pack(fill="both", expand=True)
        # TODO: figure out why label won't pack
        # self.Label_10 = ttk.Label(self.frame_10)
        # self.Label_10.configure(text="Please be patient as this may take some time")
        # self.Label_10.pack()
        self.Submenu_00.entryconfig(0, state="disabled")

        def run_thread(_self):
            _self.progress.start()
            _self.kwargs.get("menu_01")()
            _self.progress.stop()
            _self.new_win.destroy()
            _self.Submenu_00.entryconfig(0, state="normal")

        threading.Thread(target=run_thread, args=(self,)).start()

    def menu_02(self):
        self.new_win = tk.Toplevel()
        self.new_win.geometry("300x50")
        self.new_win.resizable(False, False)
        self.new_win.title("Processing")
        self.frame_20 = ttk.LabelFrame(self.new_win)
        self.frame_20.configure(text="Updating VirusTotal Cache", padding=6)
        self.frame_20.pack(fill="both", expand=True)
        self.progress = ttk.Progressbar(self.frame_20)
        self.progress.configure(orient="horizontal", mode="indeterminate")
        self.progress.pack(fill="both", expand=True)
        # TODO: figure out why label won't pack
        # self.Label_20 = ttk.Label(self.frame_20)
        # self.Label_20.configure(text="Please be patient as this may take some time")
        # self.Label_20.pack()
        self.Submenu_00.entryconfig(1, state="disabled")

        def run_thread(_self):
            _self.progress.start()
            _self.kwargs.get("menu_02")()
            _self.progress.stop()
            _self.new_win.destroy()
            _self.Submenu_00.entryconfig(1, state="normal")

        threading.Thread(target=run_thread, args=(self,)).start()

    def menu_03(self):
        self.kwargs.get("menu_03")()

    # def test_treeview_01_select(self, event):
    #     for value in self.treeview_01.selection():
    #         print(self.treeview_01.item(value)["values"])
    #     if len(self.treeview_01.selection()) == 1:
    #         self.treeview_01_var.set(self.treeview_01.item(value)["values"][0])
    #         print(self.treeview_01_var.get())

    def test_treeview_01_insert(self, _filter=None):
        # TODO: FILTER IMPLEMENTATION
        """
        Must be a "for yield" loop
        must    yield (
                parent_value,
                index_value,
                values=(
                    _key,
                    vt_cache[_key]["data"]["attributes"]["reputation"],
                    local_cache.get(_key)["filepath"],
                    )
                )
        """
        # test case: treeview integration with scrollbar
        # for num in range(100):
        #     yield ('', 0, (num, 2, 3, 4))
        # test implementation
        self.vt_cache = self.kwargs.get("vt_cache")()
        self.local_cache = self.kwargs.get("local_cache")()

        for key in self.vt_cache:
            if (
                key == "CreationDate"
                or type(self.vt_cache[key]) != dict
                or self.vt_cache[key].get("error", None)
                or len(key) != 32
            ):
                continue
            # vt_score = vt_cache[key].get["data"]["attributes"]["reputation"]
            vt_score = self.vt_cache[key].get("data")
            if vt_score:
                vt_score = vt_score.get("attributes")
                if vt_score:
                    vt_score = vt_score.get("reputation")

            # Logic to change labels
            if vt_score < 0:
                num = self.Label_04_var.get() + 1
                self.Label_04_var.set(num)
            elif vt_score >= 0 and vt_score <= 100:
                num = self.Label_05_var.get() + 1
                self.Label_05_var.set(num)
            elif vt_score > 100:
                num = self.Label_06_var.get() + 1
                self.Label_06_var.set(num)
            elif not vt_score:
                pass

            # local_cache.get(key)["filepath"]
            local_path = self.local_cache.get(key)
            if local_path:
                local_path = local_path.get("filepath")

            # vt_cache[key]["data"]["attributes"]["first_submission_date"]
            vt_age = self.vt_cache[key].get("data")
            if vt_age:
                vt_age = vt_age.get("attributes")
                if vt_age:
                    vt_age = vt_age.get("first_submission_date")
            vt_age = datetime.fromtimestamp(vt_age)
            vt_age = vt_age.date()
            yield (
                "",
                0,
                (
                    key,
                    vt_score,
                    vt_age,
                    local_path,
                ),
            )


def test_local_cache() -> dict:
    return {"test": {"filepath": "Directory"}}


def test_vt_cache() -> dict:
    return {"test": {"data": {"attributes": {"reputation": 0}}}}


def test_button():
    print("do thing")


def test_menu_option():
    print("do thing")


if __name__ == "__main__":
    main()
