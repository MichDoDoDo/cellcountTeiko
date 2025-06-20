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
                db.LoadData(dataPath)
                print("1 to add")
                print("2 to remove")
                choice = input()
                if(choice == "1"):
                    dataPath = "cell_data/additionalCellData.csv"
                    db.AddData(dataPath)
                elif(choice == "2"):
                    print("what sample ID")
                    sample_id = input()
                    db.RemoveData(sample_id)
                else:
                    flag = False
                continue 
            case "2":
                flag = False
                continue
        
    


if __name__ == "__main__":
    main()