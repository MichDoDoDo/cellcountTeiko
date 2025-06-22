# cellcountTeiko

**Test Project.

---

## Getting Started

### Requirements

- Python 3.10+
- pip (Python package manager)

### Install Dependencie
```bash
pip install -r requirements.txt
```
### Users
1. Clone repo to local computer
2. Open Run Install Dependencies
3. Tranverse to cell_data_analysis and run
   ```bash
   python runapp.py
   ```
4. At anypoint in time if you would like to view Database locate cell_store.db and export to https://inloop.github.io/sqlite-viewer/ 
   

## Database Design
### Sample Table
| Column                      | Type    | Description                     |
| --------------------------- | ------- | ------------------------------- |
| `sample_id`                 | TEXT    | Unique ID for each sample       |
| `project`                   | TEXT    | Project the sample belongs to   |
| `subject`                   | TEXT    | Subject identifier              |
| `condition`                 | TEXT    | Disease type (e.g., melanoma)   |
| `age`                       | INTEGER | Age of subject                  |
| `sex`                       | TEXT    | 'M' or 'F'                      |
| `treatment`                 | TEXT    | Treatment type (e.g., miraclib) |
| `response`                  | TEXT    | 'yes' or 'no'                   |
| `sample_type`               | TEXT    | Sample source (e.g., PBMC)      |
| `time_from_treatment_start` | INTEGER | Timepoint of sample collection  |

### CellData Table 
| Column       | Type    | Description                        |
| ------------ | ------- | ---------------------------------- |
| `id`         | INTEGER | Primary key                        |
| `sample`     | TEXT    | Foreign key                        |
| `population` | TEXT    | Immune cell type                   |
| `count`      | INTEGER | Raw count of cells                 |

### Frequencies Table
| Column        | Type    | Description                        |
| ------------- | ------- | ---------------------------------- |
| `sample`      | TEXT    | Foreign key 
| `population`  | TEXT    | Immune cell type                   |
| `count`       | INTEGER | Raw count                          |
| `total_count` | INTEGER | Sum of all 5 immune types          |
| `percentage`  | REAL    | Relative frequency (%)             |



## Code Base Structure:
The project uses a modular design that separates database logic (db/), data analysis and I/O operations (src/), and user interface components (gui/views/). The Tkinter GUI is structured as a multi-page application with reusable views and tabbed navigation, making it easy to scale with new analytical features or database extensions.
This design was chosen to ensure clarity, maintainability, and future scalability—allowing scientists and developers to easily expand the application with minimal coupling between components.
cellcountTeiko/
- runapp.py
- db/
    - cell_data_repo.py
- gui/
    - views/
      - import_page.py
      - home_page.py
      - edit_tab.py
      - report_tab.py
- src/
    - database.py
    - data_report.py
    - db_controller.py
    
