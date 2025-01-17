import sqlite3
import pandas as pd

def connect_db(db_path):
    return sqlite3.connect(db_path)

def load_data(conn):
    query = "SELECT * FROM productsales"
    return pd.read_sql_query(query, conn)

def clean_data(df):
    df = df.copy()
    df['TOTAL_SALES'] = df['RETAIL SALES'] + df['WAREHOUSE SALES']
    return df