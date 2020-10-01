#!/usr/bin/env python

import sys

def find_keys(data):

    ankle = data['Ankle']

    #Second Key Point - Point at which ankles pass hip line (becomes negative)

    negative = True
    index = 0
    while negative:
        if ankle.iloc[index] > 0:
            key_2 = index
            negative = False
        else:
            index = index + 1

    #First Key Point - Lowest Ankle Point from first point to key_2
    try: 
        key_1 = ankle.iloc[:key_2].idxmin()
    except:
        print("The data did not match the inputted orientation. Please try again.")
        sys.exit()

    # Fourth Key Point - Point at which ankles pass hips (becomes negative)

    positive = True
    index = key_2+1
    while positive:
        if ankle.iloc[index] < 0:
            key_4 = index
            positive = False
        else:
            index = index + 1

    # Third Key Point - Highest Ankle Point from key_2 to key_4

    key_3 = ankle.iloc[key_2:key_4].idxmax()


    # Fifth Key Point - Point at which toe hits minimum again (used for time calculation)

    key_5 = ankle.iloc[key_4:].idxmin()

    # Find time for complete dolphin kick

    time_total = data['t'].iloc[key_5] - data['t'].iloc[key_1]
    time_2 = data['t'].iloc[key_2] - data['t'].iloc[key_1]
    time_3 = data['t'].iloc[key_3] - data['t'].iloc[key_2]
    time_4 = data['t'].iloc[key_4] - data['t'].iloc[key_3]
    time_1 = data['t'].iloc[key_5] - data['t'].iloc[key_4]
    
    return key_1, key_2, key_3, key_4, time_1, time_2, time_3, time_4, time_total