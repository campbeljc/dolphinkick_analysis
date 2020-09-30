#!/usr/bin/env python

# Load Excel document into Data Frame. Return Data Frame and filepath of selected data.

import pandas as pd 
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import numpy as np

def To_DataFrame(orientation, select=False):

    Tk().withdraw()

    if select:
        filepath = askopenfilename()
    else:
        filepath = "/Users/jennacampbell/Desktop/dolphin/data/NT2.xlsx"

    df = pd.read_excel(filepath)

    if orientation == 'Front':
        for (columnName, columnData) in df.iteritems():
            if columnName == 't': continue
            columnData = 0 - columnData
            df[columnName] = columnData

    destination = filepath.rpartition('/')[0]
    swimmer = filepath.rpartition("/")[2].split(".")[0]

    return destination, swimmer, df