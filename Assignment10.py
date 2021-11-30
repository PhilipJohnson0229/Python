#!/usr/bin/env python3

# Philip Johnson
# Assignment 9
# create a SQL Server DB
import pyodbc
import numpy as np
import pandas as pd
import statistics

dogs = {'Mandy':'Lab',
        'Ezzy':'Morkie',
        'Banner':'Golden Doodle',
        'Lilybette':'Corkypoo',
        }
cats = {'Snowball':'White Persian',
        'Paws':'Tabby',
        'Ladybug':'Calico'
        }
birds = {'Petey':'Parakeet',
         'Polly':'Parrot',
         'War Eagle Aurea': 'Golden Eagle',
         'Fawkes':'Phoenix',
         }
#create a list of the two dictionaries
pets = [dogs, cats, birds]

df = pd.DataFrame({'cats':cats,'dogs':dogs,'birds':birds})

print(df)


