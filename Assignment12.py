#!/usr/bin/env python3

# Philip Johnson
# Assignment 12
# using matplotlib library to create and graph

import pyodbc
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# creating the fitted line

def plotfit(x, y):
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, color='orange')


plt.style.use('classic')

data = pd.read_csv('PalmerPenguins-Combined.csv')

# part 1
# plt.plot(data.CulmenLength_mm, data.CulmenDepth_mm, 'o', color='black')

x = data.dropna().CulmenLength_mm
y = data.dropna().CulmenDepth_mm

# part 2

# filtering data by species
chinstrap = data[data.Species == 'Chinstrap']
adelie = data[data.Species == 'Adelie']
gentoo = data[data.Species == 'Gentoo']

# separating data plot points by species
plt.plot(chinstrap.CulmenLength_mm, chinstrap.CulmenDepth_mm,
         'o', color='red', label='Chinstrap')
plotfit(chinstrap.dropna().CulmenLength_mm,
        chinstrap.dropna().CulmenDepth_mm)

plt.plot(adelie.CulmenLength_mm, adelie.CulmenDepth_mm,
         'v', color='green', label='Adelie ')
plotfit(adelie.dropna().CulmenLength_mm,
        adelie.dropna().CulmenDepth_mm)

plt.plot(gentoo.CulmenLength_mm, gentoo.CulmenDepth_mm,
         'x', color='blue', label='Gentoo')
plotfit(gentoo.dropna().CulmenLength_mm,
        gentoo.dropna().CulmenDepth_mm)

# show the graphic
plt.show()
