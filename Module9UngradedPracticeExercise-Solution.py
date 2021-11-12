#!/usr/bin/env python3

# createdb.py
# create a SQL Server DB
import pyodbc

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',  # use Windows Authentication
    autocommit = True
    )

def returnDB(conn):
    if(conn):
        crsr = conn.cursor()
  
    # execute the command to fetch all the data from the table emp
    crsr.execute("SELECT COUNT(culmen_length_mm) AS [# length] \
    , MIN(culmen_length_mm) AS [Minimum Culmen Length] \
    , MAX(culmen_length_mm) AS [Maximum Culmen Length] \
    , AVG(culmen_length_mm) AS [Average Culmen Length] \
    , STDEV(culmen_length_mm) AS [Stdev Culmen Length] \
    FROM palmer_penguins.dbo.penguin")
  
    # store all the fetched data in the ans variable
    ans = crsr.fetchall()

    print(ans)
    

if conn:    
   returnDB(conn)
else:
    print('could not get connection!')
