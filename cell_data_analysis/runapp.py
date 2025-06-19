#todo:
#1) prototype app as a cli prompt


from db.cell_data_repo import CellDataRepo


def main():
    print("in main")
    flag = True
    while flag:
        print("press 1 to load data")
        print("press 2 to quit")
        userInput = input()
        
        match userInput :
            case "1":
                dbPath = "cell_store.db"
                db = CellDataRepo(dbPath)
                dataPath = "cell_data/cell-count.csv"
                db.load_data(dataPath)
                continue 
            case "2":
                flag = False
                continue
        
    


if __name__ == "__main__":
    main()