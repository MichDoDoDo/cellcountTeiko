import tkinter as tk
from tkinter import filedialog, messagebox
from db.cell_data_repo import CellDataRepo

class ImportPage(tk.Frame):
    def __init__(self, parent, controller, dbObj:CellDataRepo):
        super().__init__(parent)
        self.dbObj = dbObj
        self.controller = controller
        
        
      
        label = tk.Label(self, text="Import CSV to Start", font=("Arial", 16))
        label.pack(pady=(100,100), padx = 500)

        btn = tk.Button(self, text="Select CSV", command=self.ImportCsv)
        btn.pack()

    def ImportCsv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                self.dbObj.LoadData(filepath)
                messagebox.showinfo("Success", "CSV imported. DB initialized.")
                self.controller.ShowView("homepage")
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to import: {ex}")
                
   