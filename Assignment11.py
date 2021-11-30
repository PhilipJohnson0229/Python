#!/usr/bin/env python3

# Philip Johnson
# Assignment 11
# using pandas library to create and filter through dataframes

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

    df = pd.read_sql_query('SELECT * FROM palmer_penguins.dbo.penguin', conn)

    print(df.dtypes)
    print("\n")
    print(df.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False))
    print("\n")

    df.species.unique()

    df_dataList_1 = ['Adelie']
    df_species_1 = df[df.species.isin(df_dataList_1)]

    df_dataList_2 = ['Chinstrap']
    df_species_2 = df[df.species.isin(df_dataList_2)]

    df_dataList_3 = ['Gentoo']
    df_species_3 = df[df.species.isin(df_dataList_3)]

    print("Coefficient of correlation (all species): {}".format(df['culmen_length_mm'].corr(df['culmen_depth_mm'])))
    print("Adelie coefficient of correlation: {}".format(
        df_species_1['culmen_length_mm'].corr(df_species_1['culmen_depth_mm'])))
    print("Chinstrap coefficient of correlation: {}".format(
        df_species_2['culmen_length_mm'].corr(df_species_2['culmen_depth_mm'])))
    print("Gentoo coefficient of correlation: {}".format(
        df_species_3['culmen_length_mm'].corr(df_species_3['culmen_depth_mm'])))


if conn:
    print('Successfully connected!')
    print('Data Types:')
    returnDB(conn)
    # close the connection when done
    conn.close()
else:
    print('could not get connection!')





