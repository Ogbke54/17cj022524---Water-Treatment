from lib2to3.pgen2 import driver
from multiprocessing import connection
from select import select
import pyodbc
import pandas as pd

#driver
driver = '{ODBC Driver 13 for SQL Server}'

#Servername
server_name = 'tcp:mustmust1'
database_name = 'Kene'

#Creating server URL
server = '{server_name}.database.windows.net,1433'
database = '{database_name}' 

#Password & USernames
username = 'authentication'
password = '{PASSword12?}'

#Creating new pyodbc object
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:mustmust1.database.windows.net,1433;Database=Kene;Uid=authentication;Pwd={PASSword12?};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

#Cursor Object
cursor = cnxn.cursor()

#Importing dataset from CSV
df = pd.read_csv('Data.csv')

#Specify columns we want to import
columns = ['Country or Area', 'Year', 'Value']
df_data = df[columns]

#Define select query
select_sql = "SELECT * FROM watertreatment"

#Exec the query
cursor.execute(select_sql)

#Cursor Object
print(cursor.fetchall())

#Insert Query
insert_sql = '''
    INSERT INTO watertreatment
    VALUES (?, ?, ?)
'''

#Define record sets
records = df_data.values.tolist()

#Define data types
cursor.setinputsizes(
    [
        (pyodbc.SQL_WVARCHAR, 255, 0),
        (pyodbc.SQL_WVARCHAR, 255, 0),
        (pyodbc.SQL_WVARCHAR, 255, 0)
    ]
)

#Execute insert statement
cursor.executemany(insert_sql, records)

#Commit the transactions
cursor.commit()

#CLose connection
cnxn.close()