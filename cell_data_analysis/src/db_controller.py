import pandas as pd

class DBController:
    def __init__(self):
        pass

    def load_data_to_db(csv_path, conn):
        df = pd.read_csv(csv_path)
        try:
            df.to_sql('samples', conn, if_exists='replace', index=False)
        except Exception as ex:
            print("error loading data")
