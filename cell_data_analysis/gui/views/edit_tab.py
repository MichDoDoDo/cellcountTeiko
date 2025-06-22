import tkinter as tk
from tkinter import filedialog, messagebox
from db.cell_data_repo import CellDataRepo

class EditTab(tk.Frame):
    def __init__(self, parent, dbObj:CellDataRepo,conn):
        super().__init__(parent)
        self.conn = conn
        self.dbObj = dbObj

        tk.Label(self, text="Add Samples", font=("Arial", 14)).pack(pady=10)
        addBtn = tk.Button(self, text="Import CSV", command=self.ImportCsv)
        addBtn.pack(pady=5)

        tk.Label(self, text="Remove Sample by sample_id", font=("Arial", 14)).pack(pady=20)
        self.sampleId = tk.Entry(self)
        self.sampleId.pack(pady=5)

        removeBtn = tk.Button(self, text="Remove Sample", command=self.RemoveSample)
        removeBtn.pack(pady=5)
       
    def ImportCsv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                if(self.dbObj.AddData(filepath)):
                    messagebox.showinfo("Success", "Added CSV data to existing sample database.")
                else:
                    messagebox.showinfo("Fail", "Data was not added to database")
            except Exception as ex:
                messagebox.showerror("Error", f"Failed to import: {ex}")
    
    def RemoveSample(self):
        try:
            if(self.dbObj.RemoveData(self.sampleId.get().strip())):
                messagebox.showinfo("Success", f"Removed Sample: f{self.sampleId.get().strip()} from database")
            else:
                messagebox.showinfo("Fail", f" Failed to remove Sample: f{self.sampleId.get().strip()} from database")

        except Exception as ex:
            messagebox.showerror("Error", f"Failed to remove sample: {ex}")
    