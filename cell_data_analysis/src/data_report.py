import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

class DataReport:
    
    def __init__(self, conn):
        self.conn = conn
        self.melanomaBLPBMC_DF = self.RefreshMelanomaBLPBMC_DF()
    
    def ReportMelanomaResponders(self):
        query = """SELECT f.sample, f.population, f.percentage, s.response
        FROM frequencies f
        JOIN samples s ON f.sample = s.sample
        WHERE s.sample_type = 'PBMC' AND s.treatment = 'miraclib';
        """
        df = pd.read_sql_query(query, self.conn)
        results = []

        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x="population", y="percentage", hue="response")
        plt.title("Responders vs Non-Responders PBMC (Miraclib)")
        plt.ylabel("Relative Frequency (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        for pop in df['population'].unique():
            group = df[df['population'] == pop]
            yes = group[group['response'] == 'yes']['percentage']
            no = group[group['response'] == 'no']['percentage']
            if len(yes) == 0 or len(no) == 0:
                continue 
            stat, pval = mannwhitneyu(yes, no, alternative='two-sided')
            if pval < 0.05:
                results.append(f"{pop}: Significant difference (p = {pval:.4f})")
            else:
                results.append(f"{pop}: No significant difference (p = {pval:.4f})")
        return results, plt
    
    def ReportMelanomaBaseLineSamplePerProjectQuery(self, df):
        numSamples = df['project'].value_counts()
        print(numSamples)
        return numSamples
        
    def ReportMelanomaBaseLineResponseQuery(self, df):
        yesQuery = df['response'].value_counts()['yes']
        noQuery = df['response'].value_counts()['no']
        return(yesQuery,noQuery)
        
    def ReportMelanomaBaseLineSexQuery(self, df):
        maleData = df['sex'].value_counts()['M']
        femaleData = df['sex'].value_counts()['F']
        return (maleData, femaleData)
        
    def RefreshMelanomaBLPBMC_DF(self):
        query = """SELECT * FROM samples 
        WHERE condition = 'melanoma' 
        AND sample_type = 'PBMC' 
        AND time_from_treatment_start = 0 
        AND treatment = 'miraclib' ;"""
        
        df = pd.read_sql_query(query, self.conn)
        return df
    
    def ReportMelanomaBaseLinePBMC(self):
        downloadPath = os.path.join(os.path.expanduser('~'), 'Downloads')
        fileName = 'MelanomaBaseLinePBMC.csv'
        fullPath = os.path.join(downloadPath, fileName)
        try:
            df = self.RefreshMelanomaBLPBMC_DF()
            df.to_csv(fullPath, index=False)
            return True, fullPath
        except Exception as ex:
            print("Print")
        return False
        
        
       
