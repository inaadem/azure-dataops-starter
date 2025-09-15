"""
Sample ETL pipeline: Reads a CSV from Azure Data Lake, transforms it, and writes to Azure SQL Database.
This is a simplified example for student/demo use.
"""
import pandas as pd
import pyodbc

# Placeholder: Replace with actual Azure Data Lake access code or use local file for demo
input_csv = "sample_data.csv"  # Place a sample CSV in the pipeline/ folder

df = pd.read_csv(input_csv)

# Simple transformation: uppercase all column names
df.columns = [col.upper() for col in df.columns]

# Placeholder: Replace with your Azure SQL connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your-sql-server.database.windows.net;"
    "DATABASE=studentdb;"
    "UID=sqladminuser;"
    "PWD=ChangeMe123!"
)

# Write to SQL (replace table name as needed)
with pyodbc.connect(conn_str) as conn:
    cursor = conn.cursor()
    # Create table if not exists (simple example)
    cursor.execute("""
        IF OBJECT_ID('dbo.STUDENT_DATA', 'U') IS NULL
        CREATE TABLE dbo.STUDENT_DATA (
            ID INT,
            NAME NVARCHAR(100),
            SCORE FLOAT
        )
    """)
    conn.commit()
    # Insert data
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dbo.STUDENT_DATA (ID, NAME, SCORE) VALUES (?, ?, ?)",
            int(row['ID']), row['NAME'], float(row['SCORE'])
        )
    conn.commit()
print("ETL pipeline completed!")
