# cellcountTeiko

Test Project
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
The database is designed with normalization in mind, separating metadata (samples) from measurements (cellCounts and frequencies). This avoids data redundancy and makes it easier to manage, query, and extend. Using foreign keys ensures referential integrity between related tables.

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

## Future Improvements
This project is currently at the MVP (Minimum Viable Product) stage. While it supports all core functionality,including data import, analysis, and reporting. Several enhancements are planned to improve performance, scalability, and user experience
- Add Caching Layer: To improve performance, especially with large datasets, a caching layer using technologies like Redis is planned. This will allow faster access to frequently used or computed data (e.g., summary stats, query results), reducing database load.
- Improve UI/UX: The current interface is functional but minimal. Future updates will focus on making the GUI more intuitive and user-friendly — with features like better navigation, filtering options, embedded plots, and real-time feedback.
- Asynchronous Processing: Long-running tasks like statistical analysis or batch imports will be moved to background threads or async workflows to keep the UI responsive.
