#!/usr/bin/env python3

# Philip Johnson
# Assignment 9
# create a SQL Server DB
import pyodbc
import numpy as np
import pandas as pd
import statistics

# get a connection
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'Trusted_Connection=yes;',  # use Windows Authentication
    autocommit=True
)


def returnDB(conn):
    if (conn):
        crsr = conn.cursor()

    # execute the command to fetch all the data from the table emp
    crsr.execute("SELECT culmen_length_mm AS bill_len \
    , culmen_depth_mm as bill_depth \
    FROM palmer_penguins.dbo.penguin")

    # store all the fetched data in the ans variable
    ans = list(crsr.fetchall())

    newArray = np.asarray(ans)

    # Assign data to separate print statements

    print(newArray.ndim)
    print(newArray.shape)
    print(newArray.size)
    print(newArray.dtype)
    print(newArray.itemsize)
    print(newArray.nbytes)

    df = pd.DataFrame(newArray)
    print(df.describe())

    np.nanmax(newArray, axis=0, out=arr1)
    print(arr1)


if conn:
    returnDB(conn)
    # close the connection when done
    conn.close()
else:
    print('could not get connection!')
