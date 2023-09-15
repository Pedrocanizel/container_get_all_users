import psycopg2
import pandas as pd
import json


def get_connect():
    con = psycopg2.connect(host='', database='',
                           user='', password='')
    return con


def get_lines():
    conn = get_connect()
    query = f"""select * from schema.table"""
    df = pd.read_sql_query(query, con=conn)
    rows = df.to_json(orient='records')
    rows = json.loads(rows)
    return rows
