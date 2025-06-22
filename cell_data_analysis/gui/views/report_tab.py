import tkinter as tk
from tkinter import ttk, messagebox
from db.cell_data_repo import CellDataRepo
from src.data_report import DataReport

class ReportTab(tk.Frame):
    def __init__(self, parent, dbObjt:CellDataRepo):
        super().__init__(parent)
        self.dbObj = dbObjt
        self.report = DataReport(self.dbObj.conn)

        tk.Label(self, text="Immune Cell Frequency Report", font=("Arial", 20)).pack(pady=10)

        tk.Label(self, text="Compare the differences in cell population relative frequencies of melanoma", font=("Arial", 16)).pack(pady=10)
        btn = tk.Button(self, text="Generate Boxplots and Stats", command=self.GenerateReport)
        btn.pack(pady=10)
        
        tk.Label(self, text="PBMC BASELINE", font=("Arial", 24)).pack(pady=10)
        
        tk.Label(self, text="PBMC BaseLine Time start 0 ", font=("Arial", 16)).pack(pady=10)
        btn = tk.Button(self, text="Generate and Download Data", command=self.GenerateSampleBaseline)
        btn.pack(pady=10)
        
        tk.Label(self, text="Number of Sample Per Project", font=("Arial", 16)).pack(pady=10)
        btn = tk.Button(self, text="Generate Data", command=self.GenerateSamplePerProject)
        btn.pack(pady=10)
        
        tk.Label(self, text="Number of Responders Vs Non-Responders", font=("Arial", 16)).pack(pady=10)
        btn = tk.Button(self, text="Generate data", command=self.GenterateRespVsNonResp)
        btn.pack(pady=10)
        
        tk.Label(self, text="Male vs Female baseline data", font=("Arial", 16)).pack(pady=10)
        btn = tk.Button(self, text="Generate data", command=self.GenerateMaleVsFemale)
        btn.pack(pady=10)

        self.text = tk.Text(self, height=20)
        self.text.pack(fill="both", expand=True)
        
    def GenerateReport(self):
        data,graph = self.report.ReportMelanomaResponders()
        messagebox.showinfo("Success", data)
        graph.show()
        pass
    

    def GenerateSampleBaseline(self):
        value, fullPath = self.report.ReportMelanomaBaseLinePBMC()
        if(value):
            messagebox.showinfo("Success", f"Data has been downloaded. Path:{fullPath}")

    def GenerateSamplePerProject(self):
        df = self.report.RefreshMelanomaBLPBMC_DF()
        numSamples = self.report.ReportMelanomaBaseLineSamplePerProjectQuery(df)
        messagebox.showinfo("Sample Per Project", numSamples.to_string())

    def GenterateRespVsNonResp(self):
        df = self.report.RefreshMelanomaBLPBMC_DF()
        yesRes, noRes = self.report.ReportMelanomaBaseLineResponseQuery(df)
        messagebox.showinfo("Number of Responders Vs Non-Responders", f"Responders:{yesRes}  Non-Responders:{noRes} ")
        
    def GenerateMaleVsFemale(self):
        df = self.report.RefreshMelanomaBLPBMC_DF()
        male, female = self.report.ReportMelanomaBaseLineSexQuery(df)
        messagebox.showinfo("Number of Male Vs Female", f"Male:{male}  Female:{female} ")