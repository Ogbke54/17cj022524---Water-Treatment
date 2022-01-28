import psycopg2
import pandas as pd

# to initiate connection to database
conn = psycopg2.connect(user="postgres", password="PASSword12?", host="localhost", port=5432, database="Kene")

cursor = conn.cursor()

# sql_query = """ INSERT INTO kexx ("Country", "Year", "Value") VALUES (%s,%s,%s)"""

#Importing dataset from CSV
df = pd.read_csv('Data.csv')

#Specify columns we want to import
columns = ['Country', 'Year', 'Value']
df_data = df[columns]

#Define select query
select_sql = "SELECT * FROM kexx"

#Exec the query
cursor.execute(select_sql)

#Cursor Object
print(cursor.fetchall())

#Insert Query
insert_sql = """ INSERT INTO kexx ("Country", "Year", "Value") VALUES (%s, %s, %s)"""

#Define record sets
records = df_data.values.tolist()

cursor.executemany(insert_sql, records)

conn.commit()
count = cursor.rowcount

cursor.close()
conn.close()