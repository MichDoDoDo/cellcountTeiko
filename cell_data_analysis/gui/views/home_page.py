import tkinter as tk
from tkinter import ttk
from gui.views.edit_tab import EditTab
from gui.views.report_tab import ReportTab
from db.cell_data_repo import CellDataRepo

import pandas as pd

class HomePage(tk.Frame):
    def __init__(self, parent, controller, dbObj:CellDataRepo):
        super().__init__(parent)
        self.controller = controller
        self.dbObj = dbObj
        
        self.currentPage = 0
        self.pageSize = 30

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        tableFrame = tk.Frame(self.notebook)
        self.notebook.add(tableFrame, text="Database View")

        self.tree = ttk.Treeview(tableFrame, columns=[], show='headings')
        self.tree.pack(fill="both", expand=True)

        navFrame = tk.Frame(tableFrame)
        navFrame.pack()

        tk.Button(navFrame, text="Prev", command=self.Prev).pack(side="left", padx=5)
        tk.Button(navFrame, text="Next", command=self.Next).pack(side="left", padx=5)
        
        self.notebook.add(EditTab(self.notebook, self.dbObj,self.dbObj.conn), text="Edit")
        self.notebook.add(ReportTab(self.notebook, self.dbObj),text= "Report")

        self.RefreshTable()

    def RefreshTable(self):
        offset = self.currentPage * self.pageSize
        df = pd.read_sql_query(f"SELECT * FROM samples LIMIT {self.pageSize} OFFSET {offset}", self.dbObj.conn)

        if not df.empty:
            self.tree["columns"] = list(df.columns)
            for col in df.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100)

            for row in self.tree.get_children():
                self.tree.delete(row)

            for _, row in df.iterrows():
                self.tree.insert("", "end", values=list(row))

    def Next(self):
        self.currentPage += 1
        self.RefreshTable()

    def Prev(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.RefreshTable()