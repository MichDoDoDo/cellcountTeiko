import pandas as pd

class DBController:
    def __init__(self):
        pass

    def LoadDataToDB(self, csvPath, conn):
        df = pd.read_csv(csvPath)
        try:
            sample_columns = [
                'project', 'subject', 'condition', 'age', 'sex',
                'treatment', 'response', 'sample', 'sample_type', 'time_from_treatment_start'
            ]

            cellColumns = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

            samples_df = df[sample_columns]
            samples_df.to_sql('samples', conn, if_exists='replace', index=False)
            
            cellDataRows = []
            for _, row in df.iterrows():
                for cell_type in cellColumns:
                    cellDataRows.append({
                        "samples" : row['sample'],
                        "population": cell_type,
                        "count": row[cell_type]
                    })

            cellDataDf = pd.DataFrame(cellDataRows)
            cellDataDf.to_sql('celldata', conn, if_exists='replace', index=False)
            
            conn.commit()
            print("Loaded metadata and cell counts into DB.")

        except Exception as ex:
            print(f"Error loading data. EX: {ex}")
            
    def LoadFrqData(self, conn):
        frqList = []
        cell_df = pd.read_sql_query("SELECT * FROM celldata", conn)

        grouped = cell_df.groupby("samples")

        for sample, group in grouped:
            total = group["count"].sum()
            for _, row in group.iterrows():
                frqList.append({
                    "sample": sample,
                    "total_count": total,
                    "population": row["population"],
                    "count": row["count"],
                    "percentage": (row["count"] / total) * 100
                })

        frq_df = pd.DataFrame(frqList)
        frq_df.to_sql('frequencies', conn, if_exists='replace', index=False)
        conn.commit()
    
            
    def AddDataToDB(self, csvPath, conn):
        df = pd.read_csv(csvPath)
        try:
            sampleColumns = [
                'project', 'subject', 'condition', 'age', 'sex',
                'treatment', 'response', 'sample', 'sample_type', 'time_from_treatment_start'
            ]

            cellColumns = ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']

            samplesDf = df[sampleColumns]
            
            existingSamplesQuery = "SELECT sample FROM samples"
            existingSamplesDf = pd.read_sql_query(existingSamplesQuery, conn)
            existingSamples = set(existingSamplesDf['sample'])
            
            newSamples = set(samplesDf['sample'])
            if not newSamples.isdisjoint(existingSamples):
                print("Error, duplicate sample value found. Aborting data insertion.")
                return False

            samplesDf.to_sql('samples', conn, if_exists='append', index=False)
            
            cellDataRows = []
            for index, row in df.iterrows():
                for cell_type in cellColumns:
                    cellDataRows.append({
                        "samples" : row['sample'],
                        "population": cell_type,
                        "count": row[cell_type]
                    })

            cellDataDf = pd.DataFrame(cellDataRows)
            cellDataDf.to_sql('celldata', conn, if_exists='append', index=False)
            conn.commit()
            
            frqList = []

            cell_df = pd.read_sql_query(f"SELECT * FROM celldata", conn)

            grouped = cell_df.groupby("samples")

            for sample, group in grouped:
                total = group["count"].sum()
                for _, row in group.iterrows():
                    frqList.append({
                        "sample": sample,
                        "total_count": total,
                        "population": row["population"],
                        "count": row["count"],
                        "percentage": (row["count"] / total) * 100
                    })

            frqDf = pd.DataFrame(frqList)
            frqDf.to_sql('frequencies', conn, if_exists='append', index=False)
            conn.commit()
            return True
        except Exception as ex:
            print(f"Error loading data. EX: {ex}")
    
    
    def RemoveSampleFromDB(self,sampleId, conn):
        try:
            conn.execute("DELETE FROM samples WHERE sample = ?", (sampleId,))
            conn.commit()
            return True
        except Exception as ex:
            print(f"error deleting sample {sampleId} from database. Ex:{ex}")
        return False
        