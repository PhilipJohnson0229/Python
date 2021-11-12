#!/usr/bin/env python3

# Philip Johnson
# Assignment 9
# create a SQL Server DB
import pyodbc
import statistics

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

    # Assign data to separate print statements
    print("SQL Statistics: ")
    print("Count: ", ans[0][0])
    print("MINimum: " , ans[0][1])
    print("MAXimum: ", ans[0][2])
    print("AVerage: ", ans[0][3])
    print("STDEV: ", ans[0][4])

    # select all rows from penguin db
    crsr.execute("SELECT * FROM palmer_penguins.dbo.penguin")
    result = crsr.fetchall()

    # loop through all row items and inspect the 4th index to get the length
    final_result = [list(i) for i in result]
    lengthList = []
    for lengthItem in result:
        # if the value is null then skip
        if lengthItem[3] is None:
            continue
        lengthList.append(lengthItem[3])

    # print length item data with python functions
    print()
    print("Python Statistics: ")
    print("Count: ", len(lengthList))
    print("MINimum: " , min(lengthList))
    print("MAXimum: ", max(lengthList))
    print("AVerage: ", sum(lengthList) / len(lengthList))
    print("STDEV: ", statistics.stdev(lengthList))

    
    

if conn:    
   returnDB(conn)
   # close the connection when done
   conn.close()
else:
    print('could not get connection!')
