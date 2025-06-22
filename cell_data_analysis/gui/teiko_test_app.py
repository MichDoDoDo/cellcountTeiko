import tkinter as tk
from gui.views.import_page import ImportPage
from gui.views.home_page import HomePage
from db.cell_data_repo import CellDataRepo

class App(tk.Tk):
    
    def __init__(self, dbObj:CellDataRepo):
        super().__init__()
        self.title("Teiko Analysis Tool")
        self.geometry("1920x1080")
        self.resizable(True,True)
        
        self.conn = dbObj.conn
        
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")


        self.views = {}
        
        self.views["import"] = ImportPage(self.container, self, dbObj)
        self.views["homepage"] = HomePage(self.container, self, dbObj)

        for view in self.views.values():
            view.grid(row=0, column=0, sticky="nsew")

        self.ShowView("import")
        
    def ShowView(self, name):
        self.views[name].tkraise()

