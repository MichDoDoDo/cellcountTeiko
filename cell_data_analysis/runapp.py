#todo:
#1) prototype app as a cli prompt


from db.cell_data_repo import CellDataRepo
from gui.teiko_test_app import App

def main():
    dbPath = "cell_store.db"
    repo = CellDataRepo(dbPath)
                
    app = App(repo)
    app.mainloop()

if __name__ == "__main__":
    main()