#import all requirements
import pyodbc
import pandas as pd
import pygsheets as pg

#create connector and cursor to database[dwh-bi, Varus_WAREHOUSE]
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=server_name;"
                      "Database=database_name;"
                      "usr=user_name;"
                      "pwd=password;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

#select query (in future should can select query from sql file)
query = """
SELECT *
FROM table_name
"""

#get response and put it to dataframe
df = pd.read_sql_query(query, cnxn)

#authorization on Google API via credentials.json file (got from Google API console)
gc = pg.authorize(service_file='path to json key')

#open google spreadsheets table (need to have editing permissions)
sh = gc.open_by_url('spreadsheet url')
