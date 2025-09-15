# Project Architecture

```
+-------------------+      +-------------------+      +-------------------+
| Azure Data Lake   | ---> | Azure Data Factory| ---> | Azure SQL DB      |
| Storage Gen2      |      | (Orchestrates)    |      | (Stores Processed |
| (Raw Data)        |      |                   |      | Data)             |
+-------------------+      +-------------------+      +-------------------+
        |                        ^
        |                        |
        v                        |
+-------------------+            |
| Python ETL Script |------------+
| (pipeline/)       |
+-------------------+
```

- **Data Lake**: Stores raw data (CSV, JSON, etc.)
- **Data Factory**: Orchestrates data movement and transformation
- **SQL DB**: Stores processed/cleaned data
- **Python ETL**: Example pipeline for transformation

> See `infra    /` for Terraform code and `pipeline/` for ETL example.
